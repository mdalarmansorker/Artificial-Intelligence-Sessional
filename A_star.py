from collections import deque

H = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Drobeta': 242,
    'Eforia' : 161,
    'Fagaras': 176,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 100,
    'Rimnicu': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}

class Graph:
    def __init__(self, adjac_lis):
        self.adjac_lis = adjac_lis
 
    def get_neighbors(self, v):
        return self.adjac_lis[v]
 
    # This is heuristic function which is having equal values for all nodes
    def h(self, n):
        return H[n]
 
    def a_star_algorithm(self, start, stop):
        # In this open_lst is a lisy of nodes which have been visited, but who's 
        # neighbours haven't all been always inspected, It starts off with the start 
  #node
        # And closed_lst is a list of nodes which have been visited
        # and who's neighbors have been always inspected
        open_lst = set([start])
        closed_lst = set([])
 
        # poo has present distances from start to all other nodes
        # the default value is +infinity
        poo = {}
        poo[start] = 0
 
        # par contains an adjac mapping of all nodes
        par = {}
        par[start] = start
 
        while len(open_lst) > 0:
            n = None
 
            # it will find a node with the lowest value of f() -
            for v in open_lst:
                if n == None or poo[v] + self.h(v) < poo[n] + self.h(n):
                    n = v;
 
            if n == None:
                print('Path does not exist!')
                return None
 
            # if the current node is the stop
            # then we start again from start
            if n == stop:
                reconst_path = []
 
                while par[n] != n:
                    reconst_path.append(n)
                    n = par[n]
 
                reconst_path.append(start)
 
                reconst_path.reverse()
 
                print('Path found: {}'.format(reconst_path))
                return reconst_path
 
            # for all the neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
              # if the current node is not presentin both open_lst and closed_lst
                # add it to open_lst and note n as it's par
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)
                    par[m] = n
                    poo[m] = poo[n] + weight
 
                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update par data and poo data
                # and if the node was in the closed_lst, move it to open_lst
                else:
                    if poo[m] > poo[n] + weight:
                        poo[m] = poo[n] + weight
                        par[m] = n
 
                        if m in closed_lst:
                            closed_lst.remove(m)
                            open_lst.add(m)
 
            # remove n from the open_lst, and add it to closed_lst
            # because all of his neighbors were inspected
            open_lst.remove(n)
            closed_lst.add(n)
 
        print('Path does not exist!')
        return None


# input
# n = int(input("How many nodes: "))
# node_name = input("Enter nodes' name: ").split()
# nodes = {}
adjac_lis = {
    'Arad': [('Sibiu', 140), ('Zerind', 75), ('Timisoara', 118)],
    'Zerind': [('Oradea', 71)],
    'Timisoara': [('Lugoj', 111)],
    'Lugoj': [('Mehadia',70)],
    'Mehadia': [('Drobeta', 75)],
    'Oradea': [('Sibiu', 151)],
    'Drobeta': [('Craiova', 120)],
    'Sibiu': [('Rimnicu', 80), ('Fagaras', 99)],
    'Rimnicu': [('Craiova', 146), ('Pitesti', 97)],
    'Craiova': [('Pitesti', 138)],
    'Pitesti': [('Bucharest', 101)],
    'Fagaras': [('Bucharest', 211)],
    'Bucharest': [('Giurgiu', 90), ('Urziceni', 85)],
    'Urziceni': [('Hirsova', 98), ('Vaslui', 142)],
    'Hirsova': [('Eforie', 86)],
    'Vaslui': [('Iasi', 92)],
    'Iasi': [('Neamt', 87)]   
}
# adjacect list
# adjac_lis = dict()
# for element in node_name:
#     adjac_lis[element] = []

# e = int(input("How many edges: "))
# for i in range(e):
#     u, v, w = input("Edge %d: " %(i+1)).split()
#     child = (v, int(w))
#     child2 =(u, int(w))
#     adjac_lis[u].append(child)
#     adjac_lis[v].append(child2)
# Huristic value input
# for i in range(n):
#     a, b = input("h(%d): " %(i+1)).split()
#     H.update({a:int(b)})

# Start = input("Start: ")
# End = input("Goal: ")
graph1 = Graph(adjac_lis)
graph1.a_star_algorithm('Arad', 'Bucharest')