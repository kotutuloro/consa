from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.secret_key = "BleepBloop"


@app.route('/')
def return_homepage():
    """Display the app's homepage"""

    return render_template('homepage.html')


if __name__ == '__main__':
    app.debug = True

    DebugToolbarExtension(app)

    app.run(host='0.0.0.0')
