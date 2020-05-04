import sys

#credit to https://www.bogotobogo.com/python/python_Dijkstras_Shortest_Path_Algorithm.php

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {} #no neighbors
        self.previous = None #no parent
        #distance = infinity
        self.distance = sys.maxsize
        #all nodes unvisited
        self.visited = False

    def add_neighbor(self, neighbor, weight=0): #add connection
        self.adjacent[neighbor] = weight

    def get_connections(self): #return all connections
        return self.adjacent.keys()

    def get_id(self): #return id of self
        return self.id

    def get_weight(self, neighbor): #return edge weight to neighbor
        return self.adjacent[neighbor]

    def set_distance(self, dist): #set distance of self
        self.distance = dist

    def get_distance(self): #return distance of self
        return self.distance

    def set_previous(self, prev): #set parent of self
        self.previous = prev

    def set_visited(self): #set self to visited
        self.visited = True

    def __str__(self): #return self id and id of neighbors
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def __gt__(self, other):
        self.id < other.id
