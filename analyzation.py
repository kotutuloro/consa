"""Functions for retrieving and analyzing Spotify user data"""

import spotipy


def find_spotify_artists(search_term):
    """Returns list of results for artists matching the search term"""

    # Search for artists using the term
    sp = spotipy.Spotify()
    artist_response = sp.search(search_term, type='artist', limit=5)

    # Create a list of search results
    artist_list = parse_artist_response(artist_response['artists']['items'])

    return artist_list


def get_top_artist_recs(spotify):
    """Returns list of artist recommendations using Spotify API object"""

    # Get user's top artists
    top_artists_response = spotify.current_user_top_artists(limit=10,
                                                            time_range='medium_term')
    top_artists_list = parse_artist_response(top_artists_response['items'])

    # Get artists related to each of the user's top artists
    related_artists_dict = get_artist_recs(top_artists_list)

    return related_artists_dict


def get_artist_recs(artists_list):
    """Returns list of artist recommendations using list of artist dicitonaries"""

    sp = spotipy.Spotify()

    related_artists_list = []

    # Get artists related to each of the artists in the list
    for artist_dict in artists_list:
        rel_artists_resp = sp.artist_related_artists(artist_dict['spotify_id'])
        new_rel_artists = parse_artist_response(rel_artists_resp['artists'], artist_dict['artist'])
        related_artists_list.extend(new_rel_artists)

    return related_artists_list


def parse_artist_response(artists_response, source=None):
    """Takes results of API call and returns a list of dictionaries for each artist

    Each dictionary in the returned list has a spotify ID, artist name, source, and image url"""

    results_list = []

    # Iterate through list of artist items in response
    for artist in artists_response:

        # Create dictionary for the artist
        artist_dict = {}
        artist_dict['spotify_id'] = artist['id']
        artist_dict['artist'] = artist['name']
        artist_dict['source'] = source

        # Add a url for the artist's image if available
        try:
            artist_dict['image_url'] = artist['images'][0]['url']
        except IndexError:
            artist_dict['image_url'] = None

        # Add dictionary to the list
        results_list.append(artist_dict)

    return results_list
