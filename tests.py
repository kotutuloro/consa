import unittest
import sample_apis
import songkick
import analyzation
import spotify_oauth_tools
import spotipy
import os
import model
from datetime import datetime
from server import app


class TestSongkick(unittest.TestCase):

    def test_san_francisco(self):
        SF_Metros = songkick.find_songkick_locations("San Francisco")
        self.assertIsInstance(SF_Metros, list)
        self.assertIn("SF Bay Area", SF_Metros[0]['displayName'])

    def test_nowhere(self):
        self.assertEqual(songkick.find_songkick_locations("San Francisco, TX"), [])

    def test_concert(self):
        concerts = songkick.find_songkick_concerts('1234', 'clipping.')
        self.assertIsInstance(concerts, list)


class TestAnalyzation(unittest.TestCase):

    def test_parse_artist_response(self):
        sample_response = sample_apis.top_artists
        true_result = analyzation.parse_artist_response(sample_response)
        expected_result = {'5HJ2kX5UTwN4Ns8fB5Rn1I': 'clipping.',
                           '6Tyzp9KzpiZ04DABQoedps': 'Little Dragon',
                           '0QJIPDAEDILuo8AIq3pMuU': 'M.I.A.'}

        self.assertEqual(true_result, expected_result)

    def test_add_artists_to_dict(self):
        true_result = {}
        analyzation.add_artists_to_dict(sample_apis.clipping_related_1, true_result)

        expected_result_first = {'6Jrxnp0JgqmeUX1veU591p': 'Santigold',
                                 '0S05AeePINj4CeTVMfysIu': 'Rye Rye'}

        self.assertEqual(true_result, expected_result_first)

        analyzation.add_artists_to_dict(sample_apis.clipping_related_2, true_result)

        expected_result_second = {'6Jrxnp0JgqmeUX1veU591p': 'Santigold',
                                  '0S05AeePINj4CeTVMfysIu': 'Rye Rye',
                                  '134GdR5tUtxJrf8cpsfpyY': 'Elliphant'}

        self.assertEqual(true_result, expected_result_second)


class TestSpotifyOauth(unittest.TestCase):

    def test_get_spotify_oauth(self):
        sp_oauth = spotify_oauth_tools.get_spotify_oauth()

        self.assertIsInstance(sp_oauth, spotipy.oauth2.SpotifyOAuth)
        self.assertIn('user-top-read', sp_oauth.scope)
        self.assertEqual(sp_oauth.client_id, os.getenv('SPOTIPY_CLIENT_ID'))
        self.assertEqual(sp_oauth.client_secret, os.getenv('SPOTIPY_CLIENT_SECRET'))


class TestModel(unittest.TestCase):

    def setUp(self):
        model.connect_to_db(app, "postgresql:///testconsa")
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
        self.assertIsInstance(clip.users, list)

        cakes = model.Concert.query.get(2)
        self.assertEqual(cakes.artist, 'Cakes Da Killa')
        self.assertEqual(cakes.venue, 'The New Parish')
        self.assertIsInstance(cakes.start_datetime, datetime)
        self.assertEqual(2017, cakes.start_datetime.year)

    def test_concert_create_from_form(self):
        form = {'songkick-id': u'3',
                'artist': u'Princess Nokia',
                'venue': u'Starline Social Club',
                'city': u'Oakland, CA',
                'start-datetime': u'Sat, 06 May 2017 21:00:00 GMT'}

        nokia = model.Concert.query.get(3)
        self.assertIsNone(nokia)

        success = model.Concert.create_from_form(form)
        self.assertTrue(success)
        nokia = model.Concert.query.get(3)
        self.assertIsNotNone(nokia)
        self.assertEqual(nokia.artist, 'Princess Nokia')
        self.assertIsInstance(nokia.start_datetime, datetime)

        failure = model.Concert.create_from_form({})
        self.assertFalse(failure)

    def test_users_concerts(self):
        assoc = model.UserConcert.query.first()
        self.assertEqual(assoc.user_id, 1)
        self.assertEqual(assoc.songkick_id, 1)


if __name__ == "__main__":
    unittest.main()
