"""Functions for interacting with the Songkick API"""

import os
import requests
from datetime import datetime

SONGKICK_API_URL = "http://api.songkick.com/api/3.0"


def find_songkick_locations(search_term):
    """Return list of Songkick metro areas matching search term

    Makes a GET request to Songkick API for location data using the term.
    """

    # Make GET request to Songkick API for location
    payload = {
        'query': search_term,
        'apikey': os.getenv('SONGKICK_KEY'),
    }
    loc_response = requests.get(SONGKICK_API_URL + "/search/locations.json",
                                payload)

    # Create empty list of metro areas
    metros = []

    # If request is successful, get results from the response
    if loc_response.ok:
        results = loc_response.json()['resultsPage']['results']

        # If the results are not empty, create empty list of metro ids
        if results:
            metro_id_list = []

            # Iterate over each location in results
            for loc in results['location']:
                metro = loc['metroArea']

                # If metro area has not already been added to list of metros
                if metro['id'] not in metro_id_list:

                    # Add metro area to list
                    metros.append(metro)
                    metro_id_list.append(metro['id'])

    # Return list of metro areas for each location in results
    return metros


def find_songkick_concerts(spotify_id, artist, location="sk:26330"):
    """Takes Spotify artist info and returns a list of concert dictionaries

    Makes requests to the Songkick API for upcoming events in Songkick location
    for the provided artist name"""

    songkick_key = os.getenv('SONGKICK_KEY')

    # Create empty recommendation list
    concert_recs_list = []

    # Make GET request to songkick API for this location & artist
    payload = {
        'apikey': songkick_key,
        'artist_name': artist,
        'location': location,
    }
    event_response = requests.get(SONGKICK_API_URL + "/events.json", payload)

    # If request is successful
    if event_response.ok:

        # Get list of events from response
        events = event_response.json()['resultsPage']['results'].get('event')

        # If event list not empty
        if events:

            # Iterate over event list
            for event in events:

                # Create dictionary of concert's information
                concert = {
                    'display_name': event['displayName'],
                    'songkick_id': event['id'],
                    'songkick_url': event['uri'],
                    'artist': artist,
                    'spotify_id': spotify_id,
                    'venue': event['venue']['displayName'],
                    'city': event['location']['city'],
                }

                # Set concert dict's start_datetime as datetime, or date if datetime unavailable
                if event['start']['datetime']:
                    concert['start_datetime'] = datetime.strptime(event['start']['datetime'][:-5],
                                                                  "%Y-%m-%dT%H:%M:%S")
                elif event['start']['date']:
                    concert['start_datetime'] = datetime.strptime(event['start']['date'],
                                                                  "%Y-%m-%d")

                # Add concert to recommendation list
                concert_recs_list.append(concert)

    # If request unsuccessful, print error
    else:      # pragma: no cover
        artist = artist.encode('utf-8')
        print "Failed: {}".format(artist)

    return concert_recs_list
