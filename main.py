from icalendar import Calendar, Event, vCalAddress, vText
from datetime import datetime, time, timezone, timedelta
from pathlib import Path
import os
import pytz
from tkinter import *
import tkinter as ttk
from weather import rain
from buildings import sampleBuildings, names
from time import localtime
from tkinter import filedialog as fd
from coolcal import myCal, icsConvert
import bus
from busnodes import Node

import googlemaps
from datetime import datetime

api_key_file = open("./api_keys/gmaps", "r")
api_key = api_key_file.read().strip()
api_key_file.close()

gmaps = googlemaps.Client(key=api_key)
    
def openFileDialog() -> str:
    return fd.askopenfilename()
'''end google maps stuff'''


def bruh(): #this opens a file dialogue

    # for sched in cal:
    addy = "Memorial Student Center Texas A&M"
    # addy = w.get("1.0","end-1c")
    location = gmaps.geocode(address=addy)

    # for i in range(len(location)):
    #     print(location[i])
    #     print(i)

root = Tk()
root.geometry( "500x500" )
weather = Label(text=rain())
weather.pack()

# w = Text(root, height=1, width = 500)
# w.pack()
# loadLocButton = ttk.Button(root, text="Load Location", command = bruh)
# loadLocButton.pack()

OPTIONS = sampleBuildings
OPTIONS2 = names

root = Tk()

variable = StringVar(root)
variable.set("Desired Destination") # default value

w = OptionMenu(root, variable, *OPTIONS2)
w.pack()

def show():
    if variable.get()[0] != "Desired Location":
        if variable.get() in names:
            index = names.index(variable.get())

    end_lat, end_long = OPTIONS[index][1], OPTIONS[index][2]

    weather = Label(text=bus.work(end_lat, end_long))
    weather.pack()

button = Button(root, text="", command = show)
button.pack()

root.mainloop()

