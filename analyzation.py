def parse_artist_response(artists_response):
    """Takes results of API call for artists and returns a dictionary of artists

    The returned dictionary uses Spotify IDs as keys and artist name as values"""

    artists_dict = {}

    for artist in artists_response['items']:
        artist_id = artist['id']
        artist_name = artist['name']
        artists_dict[artist_id] = artist_name

    return artists_dict


def add_artists_to_dict(artists_response, original_dict):
    """Takes results of API call for artists and returns a dictionary of artists

    The returned dictionary uses Spotify IDs as keys and artist name as values"""

    for artist in artists_response['artists']:
        artist_id = artist['id']
        artist_name = artist['name']
        original_dict[artist_id] = artist_name

    return original_dict
