import os
import spotipy
from spotipy import oauth2

from flask import Flask, render_template, flash, redirect, request
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.secret_key = "BleepBloop"


# Move into a different file
def get_spotify_oauth():
    """Reconfigured from Spotipy's util.prompt_for_user_token to return SpotifyOAuth object"""

    # Set variables for authorization
    client_id = os.getenv('SPOTIPY_CLIENT_ID')
    client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
    redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI')
    scope = 'user-library-read'

    # Create Spotipy SpotifyOauth object
    sp_oauth = oauth2.SpotifyOAuth(client_id,
                                   client_secret,
                                   redirect_uri,
                                   scope=scope)

    return sp_oauth

SPOTIFY_OAUTH = get_spotify_oauth()


@app.route('/')
def return_homepage():
    """Displays the app's homepage"""

    return render_template('homepage.html')


@app.route('/login', methods=["GET"])
def return_login_form():
    """Displays the login form"""

    return render_template('login.html')


@app.route('/login', methods=["POST"])
def log_in():
    """Logs user in"""

    ### NOT IMPLEMENTED YET
    flash('Log in feature not implemented yet')
    return redirect('/')


@app.route('/spotify-auth')
def request_authorization():
    """Redirects to user authorization for Spotify account"""

    auth_url = SPOTIFY_OAUTH.get_authorize_url()

    return redirect(auth_url)


@app.route('/callback')
def return_results():
    """Connects to Spotify API and displays results of API call

    Gets the Spotify access token if possible
    Returns redirect to homepage if unsuccessful
    Otherwise, returns results page
    """

    # Get authorization code from Spotify
    auth_code = request.args.get('code')

    # Exchange authorization code for access token
    try:
        token_info = SPOTIFY_OAUTH.get_access_token(auth_code)
        access_token = token_info.get('access_token')

    # Flash error message & return home if getting access token fails
    except oauth2.SpotifyOauthError, error:
        flash('Unable to authorize: ' + str(error))
        return redirect('/')

    # Create Spotify API object using access_token
    spotify = spotipy.Spotify(auth=access_token)

    ### DO SOMETHING WITH RESULTS
    results = spotify.current_user_saved_tracks()
    print results

    ### RETURN TEMPLATE WITH RESULTS
    return redirect('/')


if __name__ == '__main__':
    app.debug = True

    DebugToolbarExtension(app)

    app.run(host='0.0.0.0')
