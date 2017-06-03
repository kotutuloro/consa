from freezegun import freeze_time
import unittest
import server
from datetime import datetime
import model


class TestFrozenMid(unittest.TestCase):
    def setUp(self):
        model.connect_to_db(server.app, "postgresql:///testconsa")
        model.db.create_all()
        model.example_data()

        with freeze_time('2017-06-01 23:00:00', tz_offset=-7):
            model.User.future_concerts = model.db.relationship("Concert",
                                                               order_by="Concert.start_datetime",
                                                               secondary="users_concerts",
                                                               secondaryjoin=model.db.and_(model.UserConcert.songkick_id == model.Concert.songkick_id,
                                                                                           model.Concert.start_datetime > datetime.now()))
            model.User.past_concerts = model.db.relationship("Concert",
                                                             order_by="Concert.start_datetime.desc()",
                                                             secondary="users_concerts",
                                                             secondaryjoin=model.db.and_(model.UserConcert.songkick_id == model.Concert.songkick_id,
                                                                                         model.Concert.start_datetime < datetime.now()))

        server.app.config['TESTING'] = True
        server.app.config['SECRET_KEY'] = 'key'
        self.client = server.app.test_client()

        with self.client.session_transaction() as sess:
            sess['user_id'] = 2

    def tearDown(self):
        model.db.session.close()
        model.db.drop_all()

    def test_midpoint(self):
        kiko = model.User.query.get(2)

        self.assertEqual(len(kiko.concerts), 2)
        self.assertEqual(len(kiko.past_concerts), 1)
        self.assertEqual(kiko.past_concerts[0].artist, 'Cakes Da Killa')
        self.assertEqual(len(kiko.future_concerts), 1)
        self.assertEqual(kiko.future_concerts[0].artist, 'Sleigh Bells')

    def test_profile(self):
        result = self.client.get('/my-profile')
        self.assertEqual(result.status_code, 200)
        self.assertIn(': Your Profile', result.data)

        self.assertIn('<h1>Your profile</h1>', result.data)
        self.assertIn('Email: kiko@creat.er', result.data)

        self.assertIn('<b>Sleigh Bells</b>', result.data)
        self.assertIn('Outside Lands', result.data)
        self.assertIn('<input type="hidden" class="map-lat" value="35.0">', result.data)
        self.assertIn('<input type="hidden" class="map-lng" value="-123.0">', result.data)
        self.assertIn('<input type="hidden" class="songkick-id" value="3">', result.data)
        self.assertRegexpMatches(result.data, 'Fri Aug 11, 2017\s+to Sun Aug 13, 2017')
        self.assertIn('View this event on Songkick', result.data)

        self.assertNotIn('<b>Cakes Da Killa</b>', result.data)
        self.assertNotIn('Mykki Blanco &amp; Cakes Da Killa', result.data)

    def test_past(self):
        result = self.client.get('/my-profile/past')
        self.assertEqual(result.status_code, 200)
        self.assertIn(': Your Past Concerts', result.data)

        self.assertIn('<h1>Your past concerts</h1>', result.data)
        self.assertIn('Email: kiko@creat.er', result.data)

        self.assertIn('<b>Cakes Da Killa</b>', result.data)
        self.assertIn('Mykki Blanco &amp; Cakes Da Killa', result.data)
        self.assertIn('The New Parish', result.data)
        self.assertIn('src="https://i.scdn.co/image/0aee878e922c97b73cbef3aa590781a615313791"', result.data)
        self.assertRegexpMatches(result.data, 'Fri Mar 03, 2017\s+at 8:00 PM')
        self.assertIn('View this event on Songkick', result.data)

        self.assertNotIn('<b>Sleigh Bells</b>', result.data)
        self.assertNotIn('Outside Lands', result.data)


class TestFrozenEarly(unittest.TestCase):
    def setUp(self):
        model.connect_to_db(server.app, "postgresql:///testconsa")
        model.db.create_all()
        model.example_data()

        with freeze_time('2016-06-01 23:00:00', tz_offset=-7):
            model.User.future_concerts = model.db.relationship("Concert",
                                                               order_by="Concert.start_datetime",
                                                               secondary="users_concerts",
                                                               secondaryjoin=model.db.and_(model.UserConcert.songkick_id == model.Concert.songkick_id,
                                                                                           model.Concert.start_datetime > datetime.now()))
            model.User.past_concerts = model.db.relationship("Concert",
                                                             order_by="Concert.start_datetime.desc()",
                                                             secondary="users_concerts",
                                                             secondaryjoin=model.db.and_(model.UserConcert.songkick_id == model.Concert.songkick_id,
                                                                                         model.Concert.start_datetime < datetime.now()))

    def tearDown(self):
        model.db.session.close()
        model.db.drop_all()

    def test_way_past(self):
        kiko = model.User.query.get(2)
        self.assertEqual(len(kiko.past_concerts), 0)
        self.assertEqual(len(kiko.future_concerts), 2)
        self.assertEqual(kiko.future_concerts[0].artist, 'Cakes Da Killa')


class TestFrozenFuture(unittest.TestCase):
    def setUp(self):
        model.connect_to_db(server.app, "postgresql:///testconsa")
        model.db.create_all()
        model.example_data()

        with freeze_time('2018-06-01 23:00:00', tz_offset=-7):
            model.User.future_concerts = model.db.relationship("Concert",
                                                               order_by="Concert.start_datetime",
                                                               secondary="users_concerts",
                                                               secondaryjoin=model.db.and_(model.UserConcert.songkick_id == model.Concert.songkick_id,
                                                                                           model.Concert.start_datetime > datetime.now()))
            model.User.past_concerts = model.db.relationship("Concert",
                                                             order_by="Concert.start_datetime.desc()",
                                                             secondary="users_concerts",
                                                             secondaryjoin=model.db.and_(model.UserConcert.songkick_id == model.Concert.songkick_id,
                                                                                         model.Concert.start_datetime < datetime.now()))

    def tearDown(self):
        model.db.session.close()
        model.db.drop_all()

    def test_way_future(self):
        kiko = model.User.query.get(2)
        self.assertEqual(len(kiko.future_concerts), 0)
        self.assertEqual(len(kiko.past_concerts), 2)
        self.assertEqual(kiko.past_concerts[0].artist, 'Sleigh Bells')


if __name__ == "__main__":
    unittest.main()
