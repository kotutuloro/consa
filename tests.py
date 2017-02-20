import unittest
import sample_apis
import songkick
import analyzation


class TestSongkick(unittest.TestCase):

    def test_san_francisco(self):
        SF_Metros = songkick.find_songkick_locations("San Francisco")
        self.assertIs(type(SF_Metros), list)
        self.assertIn("SF Bay Area", SF_Metros[0]['displayName'])

    def test_nowhere(self):
        self.assertEqual(songkick.find_songkick_locations("San Francisco, TX"), [])

    def test_concert(self):
        concerts = songkick.find_songkick_concerts('1234', 'clipping.')
        self.assertIs(type(concerts), list)


class TestAnalyzation(unittest.TestCase):

    def test_parse_artist_response(self):
        sample_response = sample_apis.top_artists
        true_result = analyzation.parse_artist_response(sample_response)
        expected_result = {'5HJ2kX5UTwN4Ns8fB5Rn1I': 'clipping.',
                           '6Tyzp9KzpiZ04DABQoedps': 'Little Dragon',
                           '0QJIPDAEDILuo8AIq3pMuU': 'M.I.A.'}

        self.assertEqual(true_result, expected_result)

    def test_add_artists_to_dict(self):
        sample_response_first = sample_apis.clipping_related_1

        true_result = {}
        analyzation.add_artists_to_dict(sample_response_first, true_result)

        expected_result_first = {'6Jrxnp0JgqmeUX1veU591p': 'Santigold',
                                 '0S05AeePINj4CeTVMfysIu': 'Rye Rye'}

        self.assertEqual(true_result, expected_result_first)

        sample_response_second = sample_apis.clipping_related_2
        analyzation.add_artists_to_dict(sample_response_second, true_result)

        expected_result_second = {'6Jrxnp0JgqmeUX1veU591p': 'Santigold',
                                  '0S05AeePINj4CeTVMfysIu': 'Rye Rye',
                                  '134GdR5tUtxJrf8cpsfpyY': 'Elliphant'}

        self.assertEqual(true_result, expected_result_second)


if __name__ == "__main__":
    unittest.main()
