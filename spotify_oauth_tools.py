import os
from spotipy import oauth2


def get_spotify_oauth():
    """Returns SpotifyOAuth object

    Reconfigured from Spotipy's util.prompt_for_user_token()
    """

    # Set variables for authorization
    client_id = os.getenv('SPOTIPY_CLIENT_ID')
    client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
    redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI')
    scope = 'user-top-read'

    # Create Spotipy SpotifyOauth object
    sp_oauth = oauth2.SpotifyOAuth(client_id,
                                   client_secret,
                                   redirect_uri,
                                   scope=scope)
    return sp_oauth
