from icalendar import Calendar, Event, vCalAddress, vText
from datetime import datetime, time, timezone, timedelta
from pathlib import Path
import os
import pytz
from tkinter import *
import tkinter as ttk
from weather import rain
from buildings import sampleBuildings
from time import localtime
from tkinter import filedialog as fd
from coolcal import myCal, icsConvert
import bus

'''google maps stuff'''
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
    # filename = openFileDialog()
    # cal = icsConvert(filename)
    
    # for sched in cal:
    addy = "Memorial Student Center Texas A&M"
    # addy = w.get("1.0","end-1c")
    location = gmaps.geocode(address=addy)
    
    # for i in range(len(location)):
    #     print(location[i])
    #     print(i)
    
    print(location[0].keys())
    # location = location[location]
    # location = (location.lat, location.lng)
    location = (30,-100)
    print(location)

root = Tk()
root.geometry( "500x500" )
weather = Label(text=rain())
weather.pack()

w = Text(root, height=1, width = 500)
w.pack()
loadLocButton = ttk.Button(root, text="Load Location", command = bruh)
loadLocButton.pack()

isRaining = rain() #If true raining if false not raining
#time = localtime().tm_hour * 60 + localtime().tm_min


OPTIONS = sampleBuildings
 #etc

root = Tk()

variable = StringVar(root)
variable.set("Desired Destination") # default value

w = OptionMenu(root, variable, *OPTIONS)
w.pack()

# def ok():
#     print ("value is:" + variable.get())

def show():
    if str(variable.get()) != "Desired Location":

        for elem in OPTIONS:

            if variable.get() in elem.nameAbb:
                destination = elem
        end_node = (elem.lat,elem.long)
        bus.work(location[0],location[1], end_node[0],end_node[1])

button = Button(root, text="", command = show)
button.pack()

# print(variable.get())




#end_node = destination
            








root.mainloop()

