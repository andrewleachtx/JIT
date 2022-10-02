import googlemaps
from datetime import datetime

api_key_file = open("./api_keys/gmaps", "r")
api_key = api_key_file.read().strip()
api_key_file.close()

gmaps = googlemaps.Client(key=api_key)

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)

print(directions_result)

def getDirections(start: tuple, end: tuple):
    directions = {}
    
    directions["driving"] = gmaps.directions(start, end, "driving")