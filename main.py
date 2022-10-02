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
root.geometry("1200x500")
weather = Label(text=rain() + "\n", font="Helvetica, 20")
weather.pack()

OPTIONS  = sampleBuildings
OPTIONS2 = names

variable = StringVar(root)
variable.set("Desired Destination") # Default Value

w = OptionMenu(root, variable, *OPTIONS2)
w.config(font="Helvetica, 16")
w.pack()

def show():
    if variable.get()[0] != "Desired Location":
        if variable.get() in names:
            index = names.index(variable.get())

        end_lat, end_long = OPTIONS[index][1], OPTIONS[index][2]

        weather = Label(text='\n' + bus.work(end_lat, end_long))
        weather.pack()
    else:
        pass


button = Button(root, font="Helvetica, 12", text="Find Route", command=show)
button.pack()

root.mainloop()
