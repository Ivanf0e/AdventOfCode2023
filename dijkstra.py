def dijkstra(G, n): # Graph and current node
    U = {node: None for node in G.keys()} # unvisited nodes. using None as +inf as starting distances between nodes
    V = {} # visited nodes. to be filled with distance to starting node
    d0 = 0 # current distance
    U[n] = d0 # n is current node

    while True:
        for N, d in G[n].items(): # Neighbours and corresponding distances in graph 
            if N not in U: continue # no need to revisit nodes
            d1 = d0 + d # new distance
            if U[N] is None or U[N] > d1: U[N] = d1 # only update distance if new path is shorter
        V[n] = d0 # distance to current node has to be shortest distance of previous loop
        del U[n] # remove n from the unvisited list
        if not U: break # break when all nodes visited
        C = [node for node in U.items() if node[1]] # candidate nodes
        if not C: break # break when some nodes have no neighbours
        n, d0 = sorted(C, key = lambda x: x[1])[0] # select new node with shortest distance to current node
    return V

if __name__ == "__main__":
    G = {
    'B': {'A': 5, 'D': 1, 'G': 2},
    'A': {'B': 5, 'D': 3, 'E': 12, 'F' :5},
    'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
    'G': {'B': 2, 'D': 1, 'C': 2},
    'C': {'G': 2, 'E': 1, 'F': 16},
    'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
    'F': {'A': 5, 'E': 2, 'C': 16}}
    print(dijkstra(G, 'A'))