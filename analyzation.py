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

    The returned dictionary uses Spotify IDs as keys and artist name as values"""

    # Iterate through list of artists in response
    for artist in artists_response['artists']:

        # Assigns artist's name as value to key of Spotify ID in given dicitonary
        artist_id = artist['id']
        artist_name = artist['name']
        original_dict[artist_id] = artist_name
