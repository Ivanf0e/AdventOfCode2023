import numpy as np
import matplotlib.pyplot as plt

G = {i + j*1j: c for j,r in enumerate(open('2023_21a.txt')) for i,c in enumerate(r.strip())}

nx, ny = int(max([v.real for v in G])) + 1, int(max([v.imag for v in G])) + 1
n = nx # grid size, we would expect something ~n**2
N = 200
# n=11 # cannot get it working for the assymetrical example
# N=5000
e1,n1,xi = N % n, N // n, [0,40,80] # so fit polynomial at e1, e1+n1, e1+2 n1
e1,e = 6, [n*v for v in xi]
# e = [15, 21, 30, 32, 26]

s0 = [k for k,v in G.items() if v == 'S'][0]
U = [(0, s0)] # unvisited nodes to do
G[U[0][1]] = '.'
V = set() # List for visited nodes.
D = dict()
cmod = lambda x: complex(x.real%nx, x.imag%ny)

while U:          # Creating loop to visit each node
    d,u = U.pop(0) 
    if u in V: continue
    elif d > e[-1]: continue
    V.add(u)
    D[u] = d
    
    for x in [u+v for v in [1,1j,-1,-1j]]:
        if G[(y:=cmod(x))] == '.':
            U.append((d+1, x))
                
print(len([v for v in D.values() if v<=e1 and not v%2])) # 3598
b = [len([v for v in D.values() if v<=u and v%2==u%2]) for u in e]
x1 = np.linalg.solve(np.vander(e,len(e), increasing=True), b)
print(sum([int(v) * n1**j for j,v in enumerate(x1)])) # 601441063166538

x = range(0,e[-1],2)
y = [len([v for v in D.values() if v<=u and v%2==u%2]) for u in x]
yfit = [sum([v * u**j for j,v in enumerate(x1)]) for u in x]
yerr = [v-u for v,u in zip(y,yfit)]

# 2nd polynomial for each 22 lines (or 11 if we only look at even)
r = 100000000 
ya = sum([v * r**j for j,v in enumerate(x1)]) # see example. also higher uneven, and we kept simpler here with only even
q=(r//2)%11+11*4 # //2 since only even numbersc. todo determine what good start value is, and limit above search to that
x2 = np.polyfit(x[q::11],yerr[q::11],2) #,full=True to see that residual is almost zero
ya += sum([v * r**j for j,v in  enumerate(x2[::-1])])
print(ya,6694214769421436) # good enough! https://www.reddit.com/r/adventofcode/comments/18orpvg/2023_day_21_the_puzzle_input_had_some_features_to/
# todo make for all 22 periods and low numbers
fig, ax = plt.subplots(1,1)
ax.plot(x,yerr,'.') 
# ax.plot(x,yfit)
plt.show()