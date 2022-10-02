import requests

def location_function():
    response = requests.get('https://ipinfo.io/')

    loc = response.json()['loc'].split(',')

    latitude = loc[0]
    longitude = loc[1]

    return (latitude,longitude)