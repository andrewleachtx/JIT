import requests
from busnodes import Node
from datetime import datetime
import googlemaps

def work(start_lat, start_long, end_lat, end_long):
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

    start = Node("Start", start_lat, start_long)
    end   = Node("End", end_lat, end_long)

    def closestToNode(route, startNode):
        nodeCoords = [node.coords for node in bus_stops[route]]

        distance = gmaps.distance_matrix(origins=[startNode.coords], destinations=nodeCoords)
        times = []

        for i in range(len(distance["rows"][0]["elements"])):
            time_string  = distance["rows"][0]["elements"][i]["duration"]["text"]
            times.append(int(time_string.split(' ')[0]))

        minIndex = times.index(min(times))

        return (bus_stops[route][minIndex], times[minIndex])

    potential_routes, route_times = {}, []

    for route in bus_stops:
        potential_routes[route] = (closestToNode(route, start), closestToNode(route, end))

    for route in potential_routes:
        route_times.append((route, potential_routes[route][0][1] + potential_routes[route][0][1]))

    fastest_index = 1
    for time in route_times:
        if time[1] < route_times[fastest_index][1]:
            fastest_index = route_times.index(time)

    fastest_route = route_times[fastest_index][0]

    print(f"The fastest route is {fastest_route}. The closest bus stop (walking time) to you right now is {potential_routes[fastest_route][0][0].printNode()}."
          f" You should get off on {potential_routes[fastest_route][1][0].printNode()}, it is the closest stop (walking time) to your destination")