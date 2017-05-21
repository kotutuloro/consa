"""Functions for interacting with the Songkick API"""

import os
import requests
import arrow

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

        # Add the locations to our list
        metros = create_location_list(loc_response.json())

    # Return list of metro areas for each location in results
    return metros


def create_location_list(location_json):
    """Takes SK loc search results JSON and returns list of metro area dicts

    Iterates through data in JSON to return list of metro area information.
    Returns max of 5 areas and avoids repeated locations (duplicate metro ids)
    """

    metro_list = []
    results = location_json['resultsPage']['results']

    # If the results are not empty, create empty set of metro ids
    if results:
        metro_id_set = set([])

        # Iterate over each location in results
        for loc in results['location']:
            metro = loc['metroArea']

            # Return a max of 5 matching areas
            if len(metro_list) == 5:
                return metro_list

            # If metro area has not already been added to list of metros
            elif metro['id'] not in metro_id_set:

                # Add metro area to list
                metro_list.append(metro)
                metro_id_set.add(metro['id'])

    return metro_list


def find_songkick_concerts(search_dict, location="sk:26330"):
    """Takes Spotify artist info and returns a list of concert dictionaries

    Makes requests to the Songkick API for upcoming events in Songkick location
    for the provided artist name
    """

    songkick_key = os.getenv('SONGKICK_KEY')

    # Create empty recommendation list
    concert_recs_list = []

    # Make GET request to songkick API for this location & artist
    payload = {
        'apikey': songkick_key,
        'artist_name': search_dict['artist'],
        'location': location,
    }
    event_response = requests.get(SONGKICK_API_URL + "/events.json", payload)

    # If request is successful
    if event_response.ok:

        # Add the concerts to our list
        concert_recs_list = create_concert_list(event_response.json(), search_dict)

    # If request unsuccessful, print error
    else:      # pragma: no cover
        artist = search_dict['artist'].encode('utf-8')
        print "Failed: {}".format(artist)

    return concert_recs_list


def create_concert_list(event_json, search_dict):
    """Takes Songkick event search results JSON and returns list of concert dictionaries

    Also takes a dictionary of the searched artist's information
    """

    event_list = []

    # Get list of events from response
    events = event_json['resultsPage']['results'].get('event')

    # If event list not empty
    if events:

        # Iterate over event list
        for event in events:

            # Create dictionary of concert's information
            concert = {
                'display_name': event['displayName'],
                'songkick_id': event['id'],
                'songkick_url': event['uri'],
                'artist': search_dict['artist'],
                'spotify_id': search_dict['spotify_id'],
                'image_url': search_dict['image_url'],
                'venue_name': event['venue']['displayName'],
                'venue_lat': event['venue']['lat'],
                'venue_lng': event['venue']['lng'],
                'city': event['location']['city'],
                'source': search_dict['source'],
            }

            # Set concert dict's start & end date & time
            if event.get('start'):
                if event['start']['datetime']:
                    concert['start_datetime'] = arrow.get(event['start']['datetime']).datetime
                # Only use date if there's no time
                else:
                    concert['start_datetime'] = arrow.get(event['start']['date']).datetime
                    concert['start_date'] = arrow.get(event['start']['date']).date()

            if event.get('end'):
                if event['end']['datetime']:
                    concert['end_datetime'] = arrow.get(event['end']['datetime']).datetime
                # Only use date if there's no time
                else:
                    concert['end_datetime'] = arrow.get(event['end']['date']).datetime
                    concert['end_date'] = arrow.get(event['end']['date']).date()

            # Add concert to recommendation list
            event_list.append(concert)

    return event_list
