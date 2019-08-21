class Vertex(object):
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
 
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight
 
    def __str__(self):
        return str(self.id) + "connectedTo" + str([x.id for x in self.connectedTo])
 
    def getConnections(self):
        return self.connectedTo.keys()
 
    def getId(self):
        return self.id
 
    def getWeight(self,nbr):
        return self.connectedTo[nbr]
 
 
#图类
class Graph(object):
    def __init__(self):
        self.verList = {}
        self.numVertex = 0
 
    def addVertex(self,key):
        self.numVertex += 1
        newVertex = Vertex(key)
        self.verList[key] = newVertex
        return newVertex
 
    def getVertex(self,key):
        if key in self.verList:
            return self.verList[key]
        else:
            return None
 
    def __contains__(self, item):
        return item in self.verList
 
    def addEdge(self,key1,key2,weights=0):
        if key1 not in self.verList:
            self.addVertex(key1)
        if key2 not in self.verList:
            self.addVertex(key2)
        self.verList[key1].addNeighbor(self.verList[key2],weights)
 
    def getVertices(self):
        #返回所有顶点名
        return self.verList.keys()
 
    def __iter__(self):
        return iter(self.verList.values())
 
 
def test_graph():
    g = Graph()
    for i in range(6):
        g.addVertex(i)
    print(g.verList)
    g.addEdge(0,1,5)
    g.addEdge(2,1,1)
    g.addEdge(4,3,3)
    g.addEdge(5,2,4)
    g.addEdge(1,4,0)
    for key in g:
        for vertex in key.getConnections():
            print("(%s,%s)" % (key.getId(),vertex.getId()))
 
 
if __name__ == "__main__":
    test_graph()
