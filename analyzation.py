"""Functions for retrieving and analyzing Spotify user data"""

import spotipy


def find_spotify_artists(search_term):
    """Returns dictionary of results for an artist matching the search term"""

    sp = spotipy.Spotify()
    artist_response = sp.search(search_term, type='artist')

    artist_dict = parse_artist_response(artist_response['artists']['items'])

    return artist_dict


def get_artist_recs(spotify):
    """Returns dictionary of artist recommendations using Spotify API object"""

    # Get user's top artists
    top_artists_response = spotify.current_user_top_artists(limit=10,
                                                            time_range='medium_term')
    top_artists_dict = parse_artist_response(top_artists_response['items'])

    # Get artists related to each of the user's top artists
    related_artists_dict = {}
    for artist_id in top_artists_dict.keys():
        rel_artists_resp = spotify.artist_related_artists(artist_id)
        new_rel_artists = parse_artist_response(rel_artists_resp['artists'])
        related_artists_dict.update(new_rel_artists)

    return related_artists_dict


def parse_artist_response(artists_response):
    """Takes results of API call for artists and returns a dictionary of artists

    The returned dictionary uses Spotify IDs as keys and artist name as values"""

    artists_dict = {}

    # Iterate through list of artist items in response
    for artist in artists_response:

        # Assigns artist's name as value to key of Spotify ID
        artist_id = artist['id']
        artist_name = artist['name']
        artists_dict[artist_id] = artist_name

    return artists_dict
