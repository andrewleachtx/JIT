class node:
    coords = tuple
    name = str
    nextNodes = []
    
    def __init__(self, name: str, coords: tuple):
        self.coords = coords
        self.name = name
    
    def addNext(self, nextNode):
        self.nextNodes.append(nextNode)