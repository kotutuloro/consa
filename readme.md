
# Consa

**This app is deployed [here](http://consa.herokuapp.com)!**

Consa allows users to find concerts in their area for artists based on their musical interests. Authorize your Spotify account, and Consa will determine your musical interests from your account’s top artists and find more related artists using the Spotify API. No Spotify account? No problem! If you don’t want to use your top Spotify artists, you can choose specific artists to use as starting points for your concert search instead. Consa will then use the Songkick API to search for upcoming concerts for these artists in your selected metropolitan area. Registered users can save the concerts they are interested in attending and keep track of them on their profile where they can also view the concert’s location using the Google Maps API.


## Features

#### Search for your location
![Location searching][locgif]

#### Authorize your Spotify account
![Spotify authorization][authgif]

#### (Or name up to 10 artists you like)
![Artist searching][artistgif]

#### View concerts in your area
![Concert results][resultsgif]

#### Keep track of concerts you've saved
![Your profile and saved concerts][profgif]

## About the app

Consa was created by Kiko Otutuloro as their final project at Hackbright Academy.
Check Kiko out on [LinkedIn](https://www.linkedin.com/in/kotutuloro/)!

**Tech Stack**: Python, Flask, SQLAlchemy, PostgreSQL, Jinja, Javascript, jQuery, Bootstrap

**APIs Used**: Spotify, Songkick, Google Maps

[locgif]: ../screenshots/screenshots/location-search.gif
[authgif]: ../screenshots/screenshots/spotify-auth.gif
[artistgif]: ../screenshots/screenshots/artist-search.gif
[resultsgif]: ../screenshots/screenshots/results.gif
[profgif]: ../screenshots/screenshots/profile.gif
