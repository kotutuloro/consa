from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.secret_key = "BleepBloop"


@app.route('/')
def return_homepage():
    """Display the app's homepage"""

    return render_template('homepage.html')


@app.route('/login', methods=["GET"])
def return_login_form():
    """Display the login form"""

    return render_template('login.html')


if __name__ == '__main__':
    app.debug = True

    DebugToolbarExtension(app)

    app.run(host='0.0.0.0')
