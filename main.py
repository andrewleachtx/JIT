from tkinter import *
from weather import rain
from buildings import sampleBuildings, names
from tkinter import filedialog as fd
import bus
import googlemaps

# Google
api_key_file = open("./api_keys/gmaps", "r")
api_key = api_key_file.read().strip()
api_key_file.close()

gmaps = googlemaps.Client(key=api_key)


def openFileDialog() -> str:
    return fd.askopenfilename()


def getCurrentLocation(): # Get current location, is not called currently
    # for sched in cal:
    #     address = "Memorial Student Center Texas A&M"
    #     location = gmaps.geocode(address=addy)

    pass

root    = Tk()
root.geometry("500x500")
weather = Label(text=rain())
weather.pack()

OPTIONS  = sampleBuildings
OPTIONS2 = names

root = Tk()
root.geometry("500x500")

variable = StringVar(root)
variable.set("Desired Destination") # Default Value

w = OptionMenu(root, variable, *OPTIONS2)
w.pack()

def show():
    if variable.get()[0] != "Desired Location":
        if variable.get() in names:
            index = names.index(variable.get())

    end_lat, end_long = OPTIONS[index][1], OPTIONS[index][2]

    weather = Label(text=bus.work(end_lat, end_long))
    weather.pack()


button = Button(root, text="", command=show)
button.pack()

root.mainloop()
