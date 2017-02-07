import os
import spotipy
from spotipy import oauth2

from flask import Flask, render_template, flash, redirect, request
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.secret_key = "BleepBloop"


# Move into a different module
def get_spotify_oauth():
    """Reconfigured from Spotipy's util.prompt_for_user_token
        to return SpotifyOAuth object
    """

    client_id = os.getenv('SPOTIPY_CLIENT_ID')
    client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
    redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI')
    scope = 'user-library-read'

    sp_oauth = oauth2.SpotifyOAuth(client_id, client_secret, redirect_uri, scope=scope)

    return sp_oauth

SPOTIFY_OAUTH = get_spotify_oauth()


@app.route('/')
def return_homepage():
    """Display the app's homepage"""

    return render_template('homepage.html')


@app.route('/login', methods=["GET"])
def return_login_form():
    """Display the login form"""

    return render_template('login.html')


@app.route('/login', methods=["POST"])
def log_in():
    """Log user in"""

    # Not implemented yet
    flash('Log in feature not implemented yet')
    return redirect('/')


@app.route('/spotify-auth')
def request_authorization():
    """Request user authorization for Spotify account"""

    auth_url = SPOTIFY_OAUTH.get_authorize_url()

    return redirect(auth_url)


@app.route('/callback')
def get_spotify_token():
    """Get the Spotify access token"""

    code = request.args.get('code')

    try:
        token_info = SPOTIFY_OAUTH.get_access_token(code)
    except oauth2.SpotifyOauthError, error:
        flash('Unable to authorize: ' + str(error))
        return redirect('/')

    if token_info:
        access_token = token_info['access_token']
    else:
        access_token = None

    if access_token:
        sp = spotipy.Spotify(auth=access_token)
        results = sp.current_user_saved_tracks()
        # DO SOMETHING WITH RESULT THNX

    else:
        print "Can't get token"

    return redirect('/')

if __name__ == '__main__':
    app.debug = True

    DebugToolbarExtension(app)

    app.run(host='0.0.0.0')
