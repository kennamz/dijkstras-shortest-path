import dijkstra
import graph
import vertex


g = graph.Graph()

while (True):
    while_input = input("Enter 'e' to run the example, 'f' to load from a file, or 'c' to input from the command line: ")
    if (while_input == 'e' or while_input == 'E'):

        g.add_edge('a', 'b', 7)
        g.add_edge('a', 'c', 9)
        g.add_edge('a', 'f', 14)
        g.add_edge('b', 'c', 10)
        g.add_edge('b', 'd', 15)
        g.add_edge('c', 'd', 11)
        g.add_edge('c', 'f', 2)
        g.add_edge('d', 'e', 6)
        g.add_edge('e', 'f', 9)

        print('Graph data:')
        for v in g:
            for w in v.get_connections():
                vid = v.get_id()
                wid = w.get_id()
                print(vid, wid, v.get_weight(w))

        dijkstra.dijkstra(g, g.get_vertex('a'), g.get_vertex('e'))

        target = g.get_vertex('e')
        path = [target.get_id()]
        dijkstra.shortest(target, path)
        print('The shortest path:', path[::-1])

        break

    elif (while_input == 'f' or while_input == 'F'):
        file = open("cities.txt", "r")
        for line in file:
            args = line.split()
            src = args[0]
            dest = args[1]
            weight = int(args[2])
            g.add_edge(src, dest, weight)

        print_yesno = input("Print the list of all cities? y or n: ")
        if (print_yesno == 'y'):
            for i in g.get_vertices():
                print(i)

        begin = input("What city would you like to travel from? ")
        end = input("What city would you like to travel to? ")
        dijkstra.dijkstra(g, g.get_vertex(begin), g.get_vertex(end))

        target = g.get_vertex(end)
        path = [target.get_id()]
        dijkstra.shortest(target, path)
        print('The shortest path:', path[::-1])

        break

    elif (while_input == 'c' or while_input == 'C'):

        commandInput = input("Enter a node in the form {node1} {node2} {weight} or enter q when finished: ")
        while (commandInput != 'q'):
            args = commandInput.split()
            src = args[0]
            dest = args[1]
            weight = int(args[2])
            g.add_edge(src, dest, weight)

            commandInput = input("Enter a node in the form {node1} {node2} {weight} or enter q when finished: ")

        begin = input("What node would you like to travel from? ")
        end = input("What node would you like to travel to? ")
        dijkstra.dijkstra(g, g.get_vertex(begin), g.get_vertex(end))

        target = g.get_vertex(end)
        path = [target.get_id()]
        dijkstra.shortest(target, path)
        print('The shortest path:', path[::-1])

        break

    else:
        print("Invalid character. Try again.")


