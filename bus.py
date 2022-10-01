import requests

route_numbers = []
response = requests.get("https://transport.tamu.edu/BusRoutesFeed/api/routes")
for item in response.json():
    if not item["Group"]["IsGameDay"]:
        route_numbers.append(item["ShortName"])

bus_stops = {}

# Pull estimate time

for routeNum in route_numbers:
    response = requests.get(
        f"https://transport.tamu.edu/BusRoutesFeed/api/route/{routeNum}/pattern/2022-10-01")  # The date can be outdated, this can be changed using datetime module

    bus_stops[routeNum] = {}

    for stop in response.json():
        if stop["Name"] != "Way Point":
            if stop["Stop"]["IsTimePoint"]:
                stop_name = stop["Name"]
                latitude, longitude = stop["Latitude"], stop["Longtitude"]

                bus_stops[routeNum][stop_name] = {"Latitude": latitude, "Longitude": longitude}

print(bus_stops)