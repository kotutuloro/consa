"""Functions for retrieving and analyzing Spotify user data"""


def get_artist_recs(spotify):
    """Returns dictionary of artist recommendations using Spotify API object"""

    # Get user's top artists
    top_artists_response = spotify.current_user_top_artists(limit=3,
                                                            time_range='medium_term')
    top_artists_dict = parse_artist_response(top_artists_response)

    # Get artists related to user's top artists
    related_artists_dict = {}
    for artist_id in top_artists_dict.keys():
        rel_artists_resp = spotify.artist_related_artists(artist_id)
        add_artists_to_dict(rel_artists_resp, related_artists_dict)

    return related_artists_dict


def parse_artist_response(artists_response):
    """Takes results of API call for top artists and returns a dictionary of artists

    The returned dictionary uses Spotify IDs as keys and artist name as values"""

    artists_dict = {}

    # Iterate through list of artist items in response
    for artist in artists_response['items']:

        # Assigns artist's name as value to key of Spotify ID
        artist_id = artist['id']
        artist_name = artist['name']
        artists_dict[artist_id] = artist_name

    return artists_dict


def add_artists_to_dict(artists_response, original_dict):
    """Adds artists from results of API call for related artists to a dictionary

    The dictionary uses Spotify IDs as keys and artist name as values"""

    # Iterate through list of artists in response
    for artist in artists_response['artists']:

        # Assigns artist's name as value to key of Spotify ID in given dicitonary
        artist_id = artist['id']
        artist_name = artist['name']
        original_dict[artist_id] = artist_name
