from bus_stop import BusStop

class BusRoute:
    number = int
    stops = [BusStop]
    distToNext = []
    
    def __init__(self, number):
        self.number = number
        self.stops = []

    def addStop(self, stop: BusStop): #tuple is (name (str), coord (float,float))
        if(stop not in self.stops):
            self.stops.append(stop)
    
    def calcDistance(self):
        i = 0
        
        while(i<len(self.stops)):
            self.distToNext.append()