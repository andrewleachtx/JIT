import requests
from busnodes import Node
from datetime import datetime

route_numbers = []
response = requests.get("https://transport.tamu.edu/BusRoutesFeed/api/routes")
for item in response.json():
    if not item["Group"]["IsGameDay"]:
        route_numbers.append(item["ShortName"])

bus_stops = {}
current_date = datetime.now().strftime("%Y-%m-%d")

for routeNum in route_numbers:
    response = requests.get(
        f"https://transport.tamu.edu/BusRoutesFeed/api/route/{routeNum}/pattern/{current_date}")  # The date can be outdated, this can be changed using datetime module

    bus_stops[routeNum] = []

    for stop in response.json():
        if stop["Name"] != "Way Point":
            if stop["Stop"]["IsTimePoint"]:
                stop_name = stop["Name"]
                latitude  = (int(stop["Latitude"]) / 100000 - 5.2135)
                longitude = (int(stop["Longtitude"]) / 100000 + 10.905)

                bus_stops[routeNum].append(Node(stop_name, latitude, longitude))

def printDistances():
    for route in bus_stops:
        print(f"{route}:")

        for i in range(len(bus_stops[route]) - 1):
            currStop, nextStop = bus_stops[route][i], bus_stops[route][i + 1]

            dist = currStop.distance(nextStop)
            print(f"{currStop.stop_name} to {nextStop.stop_name} is {dist}")

        print('\n')