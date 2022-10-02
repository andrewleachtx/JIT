from busnodes import Node as node
import gmaps
 
class graph:
    nodes = {}
    
    def __init__(self, nodes: list):
        self.nodes = nodes

    def combineNodes(self, nodes: list):
        for node in nodes:
            if node in self.nodes:
                self.nodes[node.name].nextNodes = self.nodes[node.name].nextNodes 
                + node.nextNodes
            else:
                self.nodes[node.name].nextNodes = node
    
    def findNearestNodes(self, start: node, end: node):
        stops = []
        for nd in nodes:
            stops.append(nd)
            
        e = gmaps.getDistance([start,end], [s.coords for s in stops])
        
        minStart = e[0][0]
        minStartIndex = 0
        
        minEnd = e[1][0]
        minEndIndex = 0
        
        for i in range(1, len(minEnd[0])):
            if e[0][i] < minStart:
                minStart = e[0][i]
                minStartIndex = i
            
            if e[1][i] < minEnd:
                minEnd = e[1][i]
                minEndIndex = i
        
        return (s[minStartIndex], s[minEndIndex])
    
    def returnPath(self, start, end):
        

