import vertex
import sys

#credit to https://www.bogotobogo.com/python/python_Dijkstras_Shortest_Path_Algorithm.php

class Graph:
    def __init__(self):
        self.vert_dict = {} #dictonary of verticies
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values()) #return list of all verticies

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1 #add 1 to count
        new_vertex = vertex.Vertex(node) #initialize new vertex
        self.vert_dict[node] = new_vertex #add vertex to dictionary of all verticies
        return new_vertex

    def get_vertex(self, n): #get vertex with index n
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0): #add connection
        if frm not in self.vert_dict: #add vertex if not in graph
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost) #set neighbor
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self): #return all vertices in graph
        return self.vert_dict.keys()

    def set_previous(self, current): #set parent
        self.previous = current

    def get_previous(self, current): #return parent
        return self.previous