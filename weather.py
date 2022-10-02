def rain():
    import requests
    from location import location_function
    #Currently set to location on campus. Could read in location date potentially from google maps
    latitude = location_function()[0]
    longitude = location_function()[1]

    #Translate location to necessary grid
    location = requests.get(f"https://api.weather.gov/points/{latitude},{longitude}")


    gridId = location.json()['properties']['gridId']
    gridX = location.json()['properties']['gridX']
    gridY = location.json()['properties']['gridY']


    response = requests.get(f"https://api.weather.gov/gridpoints/{gridId}/{gridX},{gridY}/forecast")

    #First Twelve Hours
    twelve = response.json()['properties']['periods'][0]["detailedForecast"]
    low = response.json()['properties']['periods'][0]["temperature"]


    #Remaining Twelve Hours of Day
    twentyfour = response.json()['properties']['periods'][1]["detailedForecast"]
    high = response.json()['properties']['periods'][1]["temperature"]


    rain = False
    if (("rain" in twelve) or ("rain" in twentyfour)):
        rain = True
    
    return rain
