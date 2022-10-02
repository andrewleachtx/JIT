# J.I.T. Just In Time

## About
In a day and age where we have to wake up daily to face the gaunlet before us, we have much that is out of our control. Wet socks from rain, a shirt drenched in sweat from the heat, traffic, absurdly long lines for your coffee, buses running off schedule, and too many more. We have a million choices to make in an instant based off of information that we cannot gather, and just like that you can ruin your entire day in that instant.

Too many unknowns, and too much chaos.

The goal of J.I.T. is to take all of the unexpected things that will ruin your day, and _expect them for you._

J.I.T. takes input from a user, such as a wake-up alarm and calendar, and will pull a mass of data accessible online about your location, the weather, traffic, etc... and after that point. J.I.T. will give you all of the information you need to decide.

## Features
- Take user input of a current location, and a desired location. From this, find of all routes the one with the least walking time required in order to get to a bus stop and get off the next bus stop closest to the destination.
- Display weather information and ask user decisions about their path.
- Intake calendar data as .ics and be able to calculate optimal routes from starting points.
- Use given information from user in making algorithm decisions.

## Dependencies
- [Python] with VSCode environment, chosen for straightforward implementation and reliance on libraries.
- [Requests] inbuilt Python HTTP library for pulling data via site connection.
- [Google API] using API key taken from [here][Google API].
- [JSON] inbuilt Python library for reading through and analyzing JSON files.
- [tkinter] Python module for GUI interaction with user input and output.

## Installation

No installation BASH exists currently, but is hoped to be implemented.

For now, implementation is as follows:

1) Install [Python]
2) Install [dependencies](https://github.com/andrewleachtx/JIT/) (import modules used in code as needed for now)
3) Run [main.py]


## Usage

For now, run [main.py]. Note there will be two tabs open, one for the current weather of the day and location printed using [tkinter]. Close this tab, and open the next.

From here you can select any Texas A&M building location from a list of TAMU buildings. This can also be implemented by providing the name or longitude/latitude of a location, but only a list is currently provided.

From here, click the button below, and it will print the route with the least time from your starting point (taken from GEO IP) and your final point (used as TAMU buildings, but can be user input). 

The search algorithm looks for every single bus stop in every route, finds the nearest one to your start, and the one to get off of on the same route. After comparing walk time calling [Google API] the search algorithm will provide you the data of route number, stop to get on, and stop to get off to minimize the time it takes to get to the destination.

[//]: # (reference links)

[tkinter]: <https://docs.python.org/3/library/tk.html>
[Python]: <https://www.python.org/>
[BeautifulSoup4]: <https://beautiful-soup-4.readthedocs.io/en/latest/>
[Requests]: <https://pypi.org/project/requests/>
[JSON]: <https://python.readthedocs.io/en/v2.7.2/library/json.html>
[Google API]: <https://github.com/googlemaps/google-maps-services-python>
[main.py]: <https://github.com/andrewleachtx/JIT/blob/main/main.py>
[GHub_readme]: <> 
[GHub_install]: <>
[GHub_scraperpy]: <> 
[GHub_linkcsv]: <>
