import graph
import sys
import heapq

#credit to https://www.bogotobogo.com/python/python_Dijkstras_Shortest_Path_Algorithm.php

def shortest(v, path): #make shortest path from parent
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path) #recursive call to get shortest of each ancestor
    return


def dijkstra(aGraph, start, target):
    # Set the distance for the start node to zero
    start.set_distance(0)

    # Put tuple pair into the priority queue
    #for each vertex in graph, put distance and vertex into the list of unvisited
    unvisited_queue = [(v.get_distance(), v) for v in aGraph]
    heapq.heapify(unvisited_queue) #make into a heap using python heap library

    while len(unvisited_queue): #while there are still vertices to visit
        # Pops a vertex with the smallest distance
        uv = heapq.heappop(unvisited_queue) #get minimum from minheap
        current = uv[1]
        current.set_visited() #vertex has now been visited

        # for next in v.adjacent:
        for next in current.adjacent: #for all neighbors
            # if visited, skip
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)

            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)

        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.get_distance(), v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)

    print("The shortest distance:", target.get_distance())