""" Gets information about the given user frinds (location, Twitter nickname) """

import requests
from pprint import pprint
import json
from geopy.geocoders import Nominatim


def search_user(nickname: str):
    """
    Looks for Twitter's user information
    """
    base_url = 'https://api.twitter.com/'
    bearer_token = 'TOKEN WAS REMOVED FOR THE SAFETY REASONS'
    search_url = f'{base_url}1.1/friends/list.json'

    search_headers = {
        'Authorization': f'Bearer {bearer_token}'
    }

    search_params  = {
        'screen_name': nickname
    }

    responce = requests.get(search_url, headers=search_headers, params=search_params)
    json_responce = responce.json()

    if 'error' in json_responce:
        return {}
    
    info = {}
    for usr in range(len(json_responce['users'])):
        location = json_responce['users'][usr]['location']
        name = json_responce['users'][usr]['screen_name']
        info[name] = location
        # print(name, location, usr)

    return info


def find_coordinates(info: dict) -> dict:
    """
    Adds coordinates as a key value instead of location.
    """
    for key in info:
        geolocator = Nominatim(user_agent="app")
        # print(key, info[key])
        if info[key] != '':
            location = geolocator.geocode(info[key])

            if location is not None:
                print(info[key])
                lat, lon = location.latitude, location.longitude
                # print(lat, lon)
                info[key] = (lat, lon)

    return {key: info[key] for key in info if isinstance(info[key], tuple)}


def main(nickname: str):
    """
    Main function of the module, returns fictionary with the
    nickname's friends on Twitter, where the nickname is a key and its value
    is location in coordinates.
    """
    info = search_user(nickname)
    info = find_coordinates(info)
    return info

if __name__ == '__main__':
    usr = '@BarackObama'
    usr2 = '@Ostap36606289'
    usr3 = '@hello'
    print(main(usr3))