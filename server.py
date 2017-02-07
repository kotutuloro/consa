import spotipy
from spotipy.oauth2 import SpotifyOauthError

from spotify_oauth_tools import get_spotify_oauth
from analyzation import *

from flask import Flask, render_template, flash, redirect, request
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.secret_key = "BleepBloop"

# Create Spotify OAuth object for use with spotipy
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
    except SpotifyOauthError, error:
        flash('Unable to authorize: ' + str(error))
        return redirect('/')

    # Create Spotify API object using access_token
    spotify = spotipy.Spotify(auth=access_token)

    # Get user's top artists
    top_artists_response = spotify.current_user_top_artists(limit=10,
                                                            time_range='medium_term')
    top_artists_dict = parse_artist_response(top_artists_response)

    # Get artists related to user's top artists
    related_artists_dict = {}

    for artist_id in top_artists_dict.keys():
        rel_artists_response = spotify.artist_related_artists(artist_id)
        related_artists_dict = add_artists_to_dict(rel_artists_response, related_artists_dict)

    print related_artists_dict

    ### RETURN TEMPLATE WITH RESULTS
    flash('Results feature not implemented yet')
    return redirect('/')


if __name__ == '__main__':
    app.debug = True

    # DebugToolbarExtension(app)

    app.run(host='0.0.0.0')
