import random
import requests
from busnodes import Node
from datetime import datetime
import googlemaps

# To be called in main.py with a parameter of latitude and longitude of a destination.
def work(end_lat, end_long):
    api_key_file = open("./api_keys/gmaps", "r")
    api_key = api_key_file.read().strip()
    api_key_file.close()

    gmaps = googlemaps.Client(key=api_key)

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
                    latitude = round((int(stop["Latitude"]) / 100000 - 5.2135), 5)
                    longitude = round((int(stop["Longtitude"]) / 100000 + 10.905), 5)

                    bus_stops[routeNum].append(Node(stop_name, latitude, longitude))


    def printDistances():
        for route in bus_stops:
            print(f"{route}:")

            for i in range(len(bus_stops[route]) - 1):
                currStop, nextStop = bus_stops[route][i], bus_stops[route][i + 1]

                dist = currStop.distance(nextStop)
                print(f"{currStop.stop_name} to {nextStop.stop_name} is {dist}")

            print('\n')

    # As we did not finish implementing a current longitude and latitude code, we will use a random generator
    random_deviation = random.uniform(-1, 1)
    start_lat, start_long = 29.119 + random_deviation, -98.3402 + random_deviation
    start = Node("Start", start_lat, start_long)
    end   = Node("End", end_lat, end_long)

    # This function takes a route, and the user inputted start.
    def closestToNode(route, startNode):
        nodeCoords = [node.coords for node in bus_stops[route]]

        distance = gmaps.distance_matrix(origins=[startNode.coords], destinations=nodeCoords)
        times = []

        for i in range(len(distance["rows"][0]["elements"])):
            time_string  = distance["rows"][0]["elements"][i]["duration"]["text"]
            times.append(float(time_string.split(' ')[0]) * 1.8)

        minIndex = times.index(min(times))

        # Returns tuple with the bus stop's name, and the time it takes.
        return (bus_stops[route][minIndex], times[minIndex])

    potential_routes, route_times = {}, []

    # For every route, add a potential route that has the closest stop to the user's current location, and the bus stop on that route that is closest to the ending position.
    for route in bus_stops:
        potential_routes[route] = (closestToNode(route, start), closestToNode(route, end))

    # For every route, find the total walking time, which includes the start to bus stop, and last bus stop to destination.
    for route in potential_routes:
        route_times.append((route, potential_routes[route][0][1] + potential_routes[route][0][1]))

    # Find the route that has the smallest walk time.
    fastest_index = 1
    for time in route_times:
        if time[1] < route_times[fastest_index][1]:
            fastest_index = route_times.index(time)

    fastest_route = route_times[fastest_index][0]

    return (f"The fastest route is {fastest_route}. The closest bus stop (walking time) to you right now is {potential_routes[fastest_route][0][0].printNode()}."
          f" You should get off on {potential_routes[fastest_route][1][0].printNode()}, it is the closest stop (walking time) to your destination")