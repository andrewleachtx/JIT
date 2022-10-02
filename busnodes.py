class Node:
    def __init__(self, name, latitude, longitude):
        self.stop_name = name
        self.coords = (latitude, longitude)

    def printNode(self):
        print(self.stop_name, self.coords)

    def distance(self, otherNode):
        latitudeDifference = abs(self.coords[0] - otherNode.coords[0])
        longitudeDifference = abs(self.coords[1] - otherNode.coords[1])

        return (latitudeDifference, longitudeDifference)