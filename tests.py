import unittest
from datetime import datetime
import spotipy
import os
# from flask import session

import sample_apis
import songkick
import analyzation
import spotify_oauth_tools
import model
import server


class TestSongkick(unittest.TestCase):

    def test_san_francisco(self):
        SF_Metros = songkick.find_songkick_locations("San Francisco")
        self.assertIsInstance(SF_Metros, list)
        self.assertIn("SF Bay Area", SF_Metros[0]['displayName'])

    def test_nowhere(self):
        self.assertEqual(songkick.find_songkick_locations("San Francisco, TX"), [])

    def test_concert(self):
        concerts = songkick.find_songkick_concerts('1234', 'Run The Jewels')
        self.assertIsInstance(concerts, list)


class TestAnalyzation(unittest.TestCase):

    def test_find_spotify_artists(self):
        result = analyzation.find_spotify_artists('Run the Jewels')
        self.assertIn('Run The Jewels', result[0]['artist'])

    def test_parse_artist_search(self):
        clip_search = sample_apis.clipping_search['artists']['items']
        result = analyzation.parse_artist_search(clip_search)

        self.assertIsInstance(result, list)
        self.assertIsInstance(result[0], dict)
        self.assertEqual(result[0]['spotify_id'], '5HJ2kX5UTwN4Ns8fB5Rn1I')
        self.assertEqual(result[0]['image_url'], 'https://i.scdn.co/image/96f3fd452d3871eea1ba9ba9cab63b002d8360bb')
        self.assertEqual(result[1]['artist'], 'Clipping')
        self.assertIsNone(result[2]['image_url'])

    def test_get_artist_recs(self):
        top_artist = {'6Tyzp9KzpiZ04DABQoedps': 'Little Dragon'}
        result = analyzation.get_artist_recs(top_artist)
        self.assertIsInstance(result, dict)
        self.assertNotEqual(len(result), 0)

    def test_parse_artist_response(self):
        sample_response = sample_apis.top_artists['items']
        true_result = analyzation.parse_artist_response(sample_response)
        expected_result = {'5HJ2kX5UTwN4Ns8fB5Rn1I': 'clipping.',
                           '6Tyzp9KzpiZ04DABQoedps': 'Little Dragon',
                           '0QJIPDAEDILuo8AIq3pMuU': 'M.I.A.'}

        self.assertEqual(true_result, expected_result)


class TestSpotifyOauth(unittest.TestCase):

    def test_get_spotify_oauth(self):
        sp_oauth = spotify_oauth_tools.get_spotify_oauth()

        self.assertIsInstance(sp_oauth, spotipy.oauth2.SpotifyOAuth)
        self.assertIn('user-top-read', sp_oauth.scope)
        self.assertEqual(sp_oauth.client_id, os.getenv('SPOTIPY_CLIENT_ID'))
        self.assertEqual(sp_oauth.client_secret, os.getenv('SPOTIPY_CLIENT_SECRET'))


class TestModel(unittest.TestCase):

    def setUp(self):
        model.connect_to_db(server.app, "postgresql:///testconsa")
        model.db.create_all()
        model.example_data()

    def tearDown(self):
        model.db.session.close()
        model.db.drop_all()

    def test_users(self):
        kiko = model.User.query.get(2)
        self.assertEqual(kiko.email, 'kiko@creat.er')
        self.assertEqual(kiko.password, 'kikokikokiko')
        self.assertIsInstance(kiko.concerts, list)
        self.assertIsInstance(kiko.concerts[0], model.Concert)

    def test_user_add_concert(self):
        noone = model.User.query.get(3)
        self.assertEqual(noone.concerts, [])

        success = noone.add_concert(2)
        self.assertTrue(success)
        self.assertNotEqual(noone.concerts, [])
        self.assertEqual(noone.concerts[0].artist, 'Cakes Da Killa')

        failure = noone.add_concert(99)
        self.assertFalse(failure)

    def test_user_remove_concert(self):
        user = model.User.query.first()
        self.assertNotEqual(user.concerts, [])
        self.assertEqual(len(user.concerts), 1)

        success = user.remove_concert(1)
        self.assertTrue(success)
        self.assertEqual(user.concerts, [])

    def test_concerts(self):
        clip = model.Concert.query.get(1)
        self.assertEqual(clip.artist, 'clipping.')
        self.assertEqual(clip.city, 'San Francisco, CA')
        self.assertIsNone(clip.songkick_url)
        self.assertEqual(clip.venue_lat, 37.7697)
        self.assertEqual(clip.venue_lng, -122.4203)
        self.assertIsInstance(clip.users, list)

        cakes = model.Concert.query.get(2)
        self.assertEqual(cakes.artist, 'Cakes Da Killa')
        self.assertEqual(cakes.venue_name, 'The New Parish')
        self.assertEqual(cakes.venue_lat, 37.8077)
        self.assertIsInstance(cakes.start_datetime, datetime)
        self.assertEqual(2017, cakes.start_datetime.year)

    def test_concert_create_from_form(self):
        form = {'songkick-id': u'3',
                'artist': u'Princess Nokia',
                'venue-name': u'Starline Social Club',
                'venue-lat': u'37.8123',
                'venue-lng': u'-122.2725',
                'city': u'Oakland, CA',
                'start-datetime': u'Sat, 06 May 2017 21:00:00 GMT'}

        nokia = model.Concert.query.get(3)
        self.assertIsNone(nokia)

        success = model.Concert.create_from_form(form)
        self.assertTrue(success)

        nokia = model.Concert.query.get(3)
        self.assertIsNotNone(nokia)
        self.assertEqual(nokia.artist, 'Princess Nokia')
        self.assertEqual(nokia.venue_lng, -122.2725)
        self.assertEqual(nokia.venue_name, 'Starline Social Club')
        self.assertIsInstance(nokia.start_datetime, datetime)

        failure = model.Concert.create_from_form({})
        self.assertFalse(failure)

    def test_users_concerts(self):
        assoc = model.UserConcert.query.first()
        self.assertEqual(assoc.user_id, 1)
        self.assertEqual(assoc.songkick_id, 1)


class TestServer(unittest.TestCase):

    def setUp(self):
        server.app.config['TESTING'] = True
        self.client = server.app.test_client()

        model.connect_to_db(server.app, "postgresql:///testconsa")
        model.db.create_all()
        model.example_data()

    def tearDown(self):
        model.db.session.close()
        model.db.drop_all()

    def test_homepage(self):
        result = self.client.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn('Consa', result.data)

        self.assertIn('Location', result.data)
        self.assertIn('<form id="spotify-auth-form">', result.data)
        self.assertIn('Use your Spotify account', result.data)

        self.assertIn('<div id="spotify-artist-search"', result.data)
        self.assertIn('Selected Artists', result.data)

    def test_nav_bar(self):
        result = self.client.get('/')
        self.assertEqual(result.status_code, 200)

        self.assertIn('Register', result.data)
        self.assertIn('Login', result.data)
        self.assertNotIn('My Profile', result.data)
        self.assertNotIn('Logout', result.data)

    def test_display_login_form(self):
        result = self.client.get('/login')
        self.assertEqual(result.status_code, 200)
        self.assertIn(': Login', result.data)

        self.assertIn('<form action="/login" method="POST">', result.data)
        self.assertIn('Email', result.data)
        self.assertIn('Password', result.data)
        self.assertNotIn('already logged in', result.data)

    def test_log_in(self):
        result = self.client.post('/login',
                                  data={'email': 'teST@tEst.ts', 'password': 'testtesttest'},
                                  follow_redirects=True)
        self.assertEqual(result.status_code, 200)

        self.assertIn('<h1>Your profile</h1>', result.data)
        self.assertIn('Email: test@test.ts', result.data)
        self.assertIn('Login successful', result.data)
        self.assertNotIn('Invalid username or password', result.data)
        # FIXME: self.assertEqual(session.get('user_id'), 1)

    def test_log_in_fail(self):
        result = self.client.post('/login',
                                  data={'email': 'test@test.ts', 'password': 'wrong'},
                                  follow_redirects=True)
        self.assertEqual(result.status_code, 200)

        self.assertIn('<form action="/login" method="POST">', result.data)
        self.assertIn('Invalid username or password', result.data)
        self.assertNotIn('<h1>Your profile</h1>', result.data)
        self.assertNotIn('Login successful', result.data)

    def test_log_out(self):
        result = self.client.get('/logout', follow_redirects=True)
        self.assertEqual(result.status_code, 200)

        self.assertNotIn('Logged out', result.data)
        self.assertIn('No user currently logged in.', result.data)
        self.assertIn('Use your Spotify account', result.data)

    def test_display_registration_form(self):
        result = self.client.get('/register')
        self.assertEqual(result.status_code, 200)
        self.assertIn(': Register', result.data)

        self.assertIn('<form action="/register" method="POST">', result.data)
        self.assertIn('Email', result.data)
        self.assertIn('Password', result.data)
        self.assertNotIn('already logged in', result.data)

    def test_register(self):
        result = self.client.post('/register',
                                  data={'email': 'new@cool.dude', 'password': 'c00ld00d'},
                                  follow_redirects=True)
        self.assertEqual(result.status_code, 200)

        self.assertIn('<h1>Your profile</h1>', result.data)
        self.assertIn('Email: new@cool.dude', result.data)
        self.assertIn('Registration successful', result.data)
        self.assertNotIn('username already exists', result.data)

    def test_register_fail(self):
        result = self.client.post('/register',
                                  data={'email': 'test@test.ts', 'password': 'lolsame'},
                                  follow_redirects=True)
        self.assertEqual(result.status_code, 200)

        self.assertIn('<form action="/register" method="POST">', result.data)
        self.assertIn('username already exists', result.data)
        self.assertNotIn('<h1>Your profile</h1>', result.data)
        self.assertNotIn('Registration successful', result.data)

    def test_profile(self):
        result = self.client.get('/my-profile', follow_redirects=True)
        self.assertEqual(result.status_code, 200)
        self.assertIn(': Login', result.data)

        self.assertIn('<form action="/login" method="POST">', result.data)
        self.assertIn('must be logged in', result.data)
        self.assertNotIn('<h1>Your profile</h1>', result.data)

    def test_callback_results_page(self):
        result = self.client.get('/callback?code=AbCdEf')
        self.assertEqual(result.status_code, 200)
        self.assertIn(': Concert Recommendations', result.data)

        self.assertIn('authCode = "AbCdEf"', result.data)
        self.assertIn('<h2>FINDING CONCERTS...</h2>', result.data)
        self.assertIn('<div id="concert-results" hidden>', result.data)

    def test_no_auth_results_page(self):
        artists = {'5HJ2kX5UTwN4Ns8fB5Rn1I': 'clipping.'}
        result = self.client.post('/no-auth-search', data=artists)
        self.assertEqual(result.status_code, 200)
        self.assertIn(': Concert Recommendations', result.data)

        self.assertIn('authCode = ""', result.data)
        self.assertIn('<h2>FINDING CONCERTS...</h2>', result.data)
        self.assertIn('<div id="concert-results" hidden>', result.data)

    def test_location_matches(self):
        result = self.client.get('/location-search?search-term=SanFrancisco,+TX')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data, '')

        result = self.client.get('/location-search?search-term=Houston')
        self.assertNotEqual(result.data, '')
        self.assertIn('"displayName": "Houston"', result.data)
        self.assertIn('"displayName": "TX"', result.data)

    def test_artist_matches(self):
        result = self.client.get('/artist-search?search-term=Run+The+Jewels')
        self.assertEqual(result.status_code, 200)
        self.assertIn('Run The Jewels', result.data)

        result = self.client.get('/artist-search?search-term=asdfasdfasdf')
        self.assertEqual(result.status_code, 200)
        self.assertEqual('', result.data)

    def test_request_authorization(self):
        result = self.client.get('/spotify-auth')
        self.assertEqual(result.status_code, 200)

        client_id = os.getenv('SPOTIPY_CLIENT_ID')
        self.assertIn(client_id, result.data)
        self.assertIn('user-top-read', result.data)
        self.assertIn('accounts.spotify.com', result.data)

    def test_recommendations(self):
        result = self.client.get('/recs?code=AbCdEf')
        self.assertEqual(result.status_code, 200)
        self.assertIn('Unable to authorize', result.data)

    def test_recs_from_search(self):
        artists = {'5HJ2kX5UTwN4Ns8fB5Rn1I': 'clipping.'}
        result = self.client.get('/recs-from-search', data=artists)
        self.assertEqual(result.status_code, 200)

    def test_concerts(self):
        result = self.client.get('/concerts?spotify-id=123&artist=clipping')
        self.assertEqual(result.status_code, 200)
        self.assertIsNotNone(result.data)


class TestServerLoggedIn(unittest.TestCase):

    def setUp(self):
        server.app.config['TESTING'] = True
        server.app.config['SECRET_KEY'] = 'key'
        self.client = server.app.test_client()

        with self.client.session_transaction() as sess:
            sess['user_id'] = 2

        model.connect_to_db(server.app, "postgresql:///testconsa")
        model.db.create_all()
        model.example_data()

    def tearDown(self):
        model.db.session.close()
        model.db.drop_all()

    def test_nav_bar(self):
        result = self.client.get('/')
        self.assertEqual(result.status_code, 200)

        self.assertIn('My Profile', result.data)
        self.assertIn('Logout', result.data)
        self.assertNotIn('Register', result.data)
        self.assertNotIn('Login', result.data)

    def test_display_login_form(self):
        result = self.client.get('/login', follow_redirects=True)
        self.assertEqual(result.status_code, 200)
        self.assertNotIn(': Login', result.data)

        self.assertNotIn('<form action="/login" method="POST">', result.data)
        self.assertIn('already logged in', result.data)
        self.assertIn('Use your Spotify account', result.data)

    def test_log_out(self):
        result = self.client.get('/logout', follow_redirects=True)
        self.assertEqual(result.status_code, 200)
        # FIXME: self.assertIsNone(session.get('user_id'))

        self.assertIn('Logged out', result.data)
        self.assertNotIn('No user currently logged in.', result.data)
        self.assertIn('Use your Spotify account', result.data)

        self.assertIn('Register', result.data)
        self.assertIn('Login', result.data)
        self.assertNotIn('My Profile', result.data)
        self.assertNotIn('Logout', result.data)

    def test_display_registration_form(self):
        result = self.client.get('/register', follow_redirects=True)
        self.assertEqual(result.status_code, 200)
        self.assertNotIn(': Register', result.data)

        self.assertNotIn('<form action="/register" method="POST">', result.data)
        self.assertIn('already logged in', result.data)
        self.assertIn('Use your Spotify account', result.data)

    def test_profile(self):
        result = self.client.get('/my-profile')
        self.assertEqual(result.status_code, 200)
        self.assertIn(': Your Profile', result.data)

        self.assertIn('<h1>Your profile</h1>', result.data)
        self.assertIn('Email: kiko@creat.er', result.data)

        self.assertIn('<b>Cakes Da Killa</b>', result.data)
        self.assertIn('Mykki Blanco &amp; Cakes Da Killa', result.data)
        self.assertIn('<input type="hidden" class="songkick-id" value="2">', result.data)
        self.assertIn('The New Parish', result.data)
        self.assertIn('{lat: 37.8077, lng: -122.2727}', result.data)
        self.assertIn('Fri Mar 03, 2017 at 8:00 PM', result.data)
        self.assertIn('View this event on Songkick', result.data)

    def test_profile_with_no_concerts(self):
        with self.client.session_transaction() as sess:
            sess['user_id'] = 3
        result = self.client.get('/my-profile')
        self.assertEqual(result.status_code, 200)
        self.assertIn(': Your Profile', result.data)

        self.assertIn('<h1>Your profile</h1>', result.data)
        self.assertIn('Email: no@one', result.data)

        self.assertNotIn('<h3>Your saved concerts</h3>', result.data)
        self.assertIn('<h3>You have no saved concerts</h3>', result.data)

    def test_add_saved_concert(self):
        success_form = {'songkick-id': u'3',
                        'artist': u'Princess Nokia',
                        'venue-name': u'Starline Social Club',
                        'city': u'Oakland, CA',
                        'start-datetime': u'Sat, 06 May 2017 21:00:00 GMT'}
        success = self.client.post('/add-concert', data=success_form)
        self.assertEqual(success.status_code, 200)
        self.assertEqual(success.data, 'True')

        user = model.User.query.get(2)
        self.assertEqual(user.concerts[1].artist, 'Princess Nokia')

        failure_form = {'songkick-id': u'99'}
        failure = self.client.post('/add-concert', data=failure_form)
        self.assertEqual(failure.status_code, 200)
        self.assertEqual(failure.data, 'False')

    def test_remove_saved_concert(self):
        result = self.client.post('/remove-concert', data={'songkick-id': '2'})
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data, 'True')

        user = model.User.query.get(2)
        self.assertEqual(user.concerts, [])


if __name__ == "__main__":
    unittest.main()
