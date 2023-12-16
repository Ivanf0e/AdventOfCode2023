from dijkstra import dijkstra

G, w = {}, open('2023_10.txt').read().split('\n')
for j,l in enumerate(w):
     for i, p in enumerate(l):
        if p == '|': # is a vertical pipe connecting north and south.
            G[(j,i)] = {(j-1,i): 1, (j+1,i): 1}
        elif p == '-': # is a horizontal pipe connecting east and west.
            G[(j,i)] = {(j,i-1): 1, (j,i+1): 1}
        elif p == 'L': # is a 90-degree bend connecting north and east.
            G[(j,i)] = {(j-1,i): 1, (j,i+1): 1}
        elif p == 'J': # is a 90-degree bend connecting north and west.
            G[(j,i)] = {(j-1,i): 1, (j,i-1): 1}
        elif p == '7': # is a 90-degree bend connecting south and west.
            G[(j,i)] = {(j+1,i): 1, (j,i-1): 1}
        elif p == 'F': # is a 90-degree bend connecting south and east.
            G[(j,i)] = {(j+1,i): 1, (j,i+1): 1}
        elif p == '.': # is ground; there is no pipe in this tile.
            pass
        elif p == 'S': # is the starting position of the animal; there is a pipe on this
            G[(j,i)] = {(j+1,i): 1, (j,i+1): 1} # S is like F
            S = (j,i)

d = dijkstra(G,S)
print(max(d.values())) # 6968

es, ds = set(), set(d.keys()) # the enclosed set to be found. loop members as set to speed up
for jj in range(j+1):
    for ii in range(i+1):
        y,x = jj, ii
        if (y,x) in ds: continue
        X = 0 # number of crossings. graphic theory says only odd number of crossings are enclosed 
        for jjj, iii in zip(range(y,j+1), range(x,i+1)):
            if (jjj, iii) in ds and not w[jjj][iii] in 'L7':
                X+=1   # at a corner perpendicular to search direction there is actual no wall crossing
        
        if X % 2 == 1: es.add((y,x,X)) # only uneven crossings are enclosed
print(len(es)) # 413

# plot
import matplotlib.pyplot as plt
import numpy as np

z = -np.ones((j+1,i+1))
for k,v in d.items():
    z[k[0]][k[1]] = v

plt.style.use('_mpl-gallery-nogrid')
fig, ax = plt.subplots()
ax.imshow(z)
plt.show()