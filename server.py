from flask import Flask, render_template, flash, redirect, request, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from passlib.hash import pbkdf2_sha256 as sha
import json

import spotipy
from spotipy.oauth2 import SpotifyOauthError

from model import User, Concert, db, connect_to_db
from spotify_oauth_tools import get_spotify_oauth

from analyzation import get_top_artist_recs, get_artist_recs, find_spotify_artists
from songkick import find_songkick_locations, find_songkick_concerts


app = Flask(__name__)

app.secret_key = "BleepBloop"

# Create Spotify OAuth object for use with spotipy
SPOTIFY_OAUTH = get_spotify_oauth()


def save_location(form):
    """Save selected location data to session from form"""

    # Get location info from form
    locID = form.get('locID')
    locName = form.get('locName')

    # Save location info to session if available
    if locID:
        session['locID'] = locID
        session['locName'] = locName


def get_user_saved_concerts():
    """Return list of current user's saved concerts"""

    # Get logged in user's user_id
    current_user_id = session.get('user_id')

    # Create list of user's saved concert's songkick ids if logged in
    if current_user_id:
        current_user = User.query.get(current_user_id)
        user_saved_concerts = [concert.songkick_id for concert in current_user.concerts]

    # Set to empty list if not logged in
    else:
        user_saved_concerts = []

    return user_saved_concerts


@app.route('/')
def return_homepage():
    """Displays the app's homepage"""

    return render_template('homepage.html')


@app.route('/login', methods=["GET"])
def return_login_form():
    """Displays the login form"""

    # If user is logged in, redirect to homepage
    if session.get('user_id'):
        flash('You are already logged in.')
        return redirect('/')

    # If user not logged in, return login form
    else:
        return render_template('login.html')


@app.route('/login', methods=["POST"])
def log_in():
    """Logs user in"""

    # Get login form data
    email = request.form.get("email").lower()
    password = request.form.get("password")

    current_user = User.query.filter_by(email=email).first()

    # If user exists in database and password is correct
    if current_user and sha.verify(password, current_user.pw_hash):

        # Set session and redirect to homepage
        session['user_id'] = current_user.user_id
        flash('Login successful')
        return redirect('/my-profile')

    # If email doesn't exist or incorrect password, inform user
    else:
        flash('Invalid username or password')
        return redirect('/login')


@app.route('/logout')
def log_out():
    """Logs user out, removing them from the Flask session"""

    # Clear session if logged in
    if session.get('user_id'):
        session.clear()
        flash('Logged out')

    # Display message if no user logged in
    else:
        flash('No user currently logged in.')

    return redirect('/')


@app.route('/register', methods=["GET"])
def return_registration_form():
    """Displays the registration form"""

    # If user is logged in, redirect to homepage
    if session.get('user_id'):
        flash('You are already logged in.')
        return redirect('/')

    # If user not logged in, return registration form
    else:
        return render_template('registration.html')


@app.route('/register', methods=["POST"])
def register():
    """Adds user to database"""

    # Get registration form data
    email = request.form.get("email").lower()
    password = request.form.get("password")

    user = User.query.filter_by(email=email).first()

    # If user already exists in database, inform user
    if user:
        flash('An account with this username already exists.')
        return redirect('/register')

    # Else add user to database
    else:
        new_user = User(email=email, pw_hash=sha.hash(password))
        db.session.add(new_user)
        db.session.commit()
        session['user_id'] = new_user.user_id

        flash('Registration successful')
        return redirect('/my-profile')


@app.route('/my-profile')
def return_user_profile():
    """Displays the profile page for the logged in user"""

    # Display user's profile page if logged in
    if session.get('user_id'):
        current_user = User.query.get(session['user_id'])
        return render_template('profile.html',
                               current_user=current_user)

    # Return redirect to login page if not logged in
    else:
        flash('You must be logged in to view your profile.')
        return redirect('/login')


@app.route('/add-concert.json', methods=["POST"])
def add_saved_concert():
    """Adds concert to user's saved list"""

    # Get concert data
    songkick_id = request.form.get('songkick-id')

    # If songkick id not already in database, insert information from post request form
    if not Concert.query.get(songkick_id):
        create_success = Concert.create_from_form(request.form)
    else:
        create_success = True

    # Get current user data
    user_id = session.get('user_id')
    current_user = User.query.get(user_id)

    # Add association between concert and current user
    add_success = current_user.add_concert(songkick_id)

    # Return T/F if successful or unsuccessful
    return jsonify(add_success and create_success)


@app.route('/remove-concert.json', methods=["POST"])
def remove_saved_concert():
    """Removes concert from user's saved list"""

    # Get concert data from AJAX request
    songkick_id = request.form.get('songkick-id')

    user_id = session.get('user_id')
    current_user = User.query.get(user_id)

    # Remove association between concert and current user
    success = current_user.remove_concert(songkick_id)

    # Return T/F if successful or unsuccessful
    return jsonify(success)


@app.route('/location-search.json')
def return_location_matches():
    """Return list of Songkick metro areas matching search

    Makes a GET request to Songkick API for location data using the data
    provided in the request to this route.
    """

    # Get search term from AJAX request
    search_term = request.args.get('search-term')

    metros = find_songkick_locations(search_term)

    # If list not empty, return a list of metro areas
    if metros:
        return jsonify(metros)

    # Return empty string if no results
    else:
        return jsonify('')


@app.route('/artist-search.json')
def return_artist_matches():
    """Return list of Spotify artists matching search"""

    # Get search term from AJAX request
    search_term = request.args.get('search-term')

    artists = find_spotify_artists(search_term)

    # If list not empty, return a list of results
    if artists:
        return jsonify(artists)

    # Return empty string if no results
    else:
        return jsonify('')


@app.route('/spotify-auth.json')
def request_authorization():
    """Saves location info and returns url for Spotify authorization"""

    # Save selected location data
    save_location(request.args)

    # Get url for Spotify authorization
    auth_url = SPOTIFY_OAUTH.get_authorize_url()

    return jsonify(auth_url)


@app.route('/callback')
def return_results_page():
    """Displays results page"""

    # Get authorization code from Spotify
    auth_code = request.args.get('code')

    # Get list of user's saved concerts
    user_saved_concerts = get_user_saved_concerts()

    return render_template('results.html',
                           auth_code=auth_code,
                           user_saved_concerts=user_saved_concerts)


@app.route('/recs.json')
def return_recommendations():
    """Connects to Spotify API and returns JSON dictionary of recommended artists

    Gets the Spotify access token if possible
    Returns error message if unsuccessful
    Otherwise, returns (JSONified) dictionary of artist recommendations
    """

    # Get auth code from callback
    auth_code = request.args.get('auth-code')

    # Exchange authorization code for access token
    try:
        token_info = SPOTIFY_OAUTH.get_access_token(auth_code)
        access_token = token_info.get('access_token')

    # Return error message if getting access token fails
    except SpotifyOauthError, error:
        return jsonify('Unable to authorize: ' + str(error))

    # Create Spotify API object using access_token
    spotify = spotipy.Spotify(auth=access_token)

    # Get dictionary of concert recommendations
    artist_recs = get_top_artist_recs(spotify)

    return jsonify(artist_recs)


@app.route('/no-auth-search', methods=['POST'])
def return_no_auth_results():
    """Saves location info and display results page"""

    # Save selected location data
    save_location(request.form)

    # Get list of artist data objects from form data
    selected_artists = request.form.get('artists')

    # Get list of user's saved concerts
    user_saved_concerts = get_user_saved_concerts()

    return render_template('results.html',
                           user_saved_concerts=user_saved_concerts,
                           selected_artists=selected_artists)


@app.route('/recs-from-search.json')
def return_recs_from_search():
    """Returns JSON dictionary of recommended artists using chosen artists"""

    # Get selected artists from form data
    selected_artists = json.loads(request.args.get('artists'))

    artist_recs = get_artist_recs(selected_artists)

    return jsonify(artist_recs)


@app.route('/concerts.json')
def return_concerts():
    """Returns JSON list of concerts for an artist and location"""

    # Get artist's spotify ID and name from request
    spotify_id = request.args.get('spotify-id')
    artist = request.args.get('artist')
    image_url = request.args.get('image-url')
    source = request.args.get('source')

    search_dict = {'spotify_id': spotify_id,
                   'artist': artist,
                   'image_url': image_url,
                   'source': source}

    # Get concert recommendations using saved location (SF Bay as default)
    locID = session.get('locID', 'sk:26330')

    concert_recs = find_songkick_concerts(search_dict, locID)

    return jsonify(concert_recs)


if __name__ == '__main__':  # pragma: no cover
    app.debug = True

    connect_to_db(app)

    DebugToolbarExtension(app)

    app.run(threaded=True)
