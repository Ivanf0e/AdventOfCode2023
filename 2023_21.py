import re
import numpy as np

G = {i + j*1j: c for j,r in enumerate(open('2023_21.txt')) for i,c in enumerate(r.strip())}

n = 131 # grid size, we would expect something ~n**2
N = 26501365
# n=11 # cannot get it working for the assymetrical example
# N=5000
e0,n1,xi = N % n, N // n, [0,1,2] # so fit polynomial at e1, e1+n1, e1+2 n1
e1,e = 64, [e0+n*v for v in xi]

U = [(0, [k for k,v in G.items() if v == 'S'][0])] # unvisited nodes to do
G[U[0][1]] = '.'
V = set() # List for visited nodes.
D = dict()
cmod = lambda x: complex(x.real%n, x.imag%n)

while U:          # Creating loop to visit each node
    d,u = U.pop(0) 
    if u in V: continue
    elif d > e[-1]: continue
    V.add(u)
    D[u] = d
    
    for x in [u+v for v in [1,1j,-1,-1j]]:
#         if x in G:
#             if G[x] == '.':
#         if (y:=cmod(x)) in G:
        if G[(y:=cmod(x))] == '.':
            U.append((d+1, x))
                
print(len([v for v in D.values() if v<=e1 and not v%2])) # 3598
b = [len([v for v in D.values() if v<=u and v%2==u%2]) for u in e]
x1 = np.linalg.solve(np.vander(xi,len(xi), increasing=True), b)
print(sum([int(v) * n1**j for j,v in enumerate(x1)])) # 601441063166538