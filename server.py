from flask import (Flask, render_template, flash, redirect, request, session)
from flask_debugtoolbar import DebugToolbarExtension

import spotipy
from spotipy.oauth2 import SpotifyOauthError

from model import (User, Concert, UserConcert, db, connect_to_db)
from spotify_oauth_tools import get_spotify_oauth
from analyzation import (parse_artist_response, add_artists_to_dict)


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

    email = request.form.get("email").lower()
    password = request.form.get("password")

    current_user = User.query.filter_by(email=email).first()

    # If user exists in database and password is correct
    if current_user and current_user.password == password:

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

    # Remove id from session if logged in
    if session.get('user_id'):
        del session['user_id']
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
        new_user = User(email=email, password=password)
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


# @app.route('/add-concert', methods=["POST"])
# def add_saved_concert():
#     """Adds concert to user's saved list"""

#     songkick_id = request.form.get('songkick-id')
#     artist = request.form.get('artist')

#     user_id = session.get('user_id')
#     current_user = User.query.get(user_id)

#     current_user.add_concert(songkick_id)

#     return redirect('/profile')


@app.route('/remove-concert', methods=["POST"])
def remove_saved_concert():
    """Removes concert from user's saved list"""

    songkick_id = request.form.get('songkick-id')

    user_id = session.get('user_id')
    current_user = User.query.get(user_id)

    current_user.remove_concert(songkick_id)

    return redirect('/profile')


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
    top_artists_resp = spotify.current_user_top_artists(limit=10,
                                                        time_range='medium_term')
    top_artists_dict = parse_artist_response(top_artists_resp)

    # Get artists related to user's top artists
    related_artists_dict = {}

    for artist_id in top_artists_dict.keys():
        rel_artists_resp = spotify.artist_related_artists(artist_id)
        print len(rel_artists_resp['artists'])
        add_artists_to_dict(rel_artists_resp, related_artists_dict)

    print len(related_artists_dict)

    ### RETURN TEMPLATE WITH RESULTS
    flash('Results feature not implemented yet')
    return redirect('/')


if __name__ == '__main__':
    app.debug = True

    connect_to_db(app)

    DebugToolbarExtension(app)

    app.run(host='0.0.0.0')
