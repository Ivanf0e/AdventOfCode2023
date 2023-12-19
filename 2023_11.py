import math
import bisect
from itertools import combinations

w = open('2023_11.txt').read().split('\n')
g = [(j,i) for j,l in enumerate(w) for i, p in enumerate(l) if p=='#']
e = [sorted(set(range(0,len(w)))-{v[k] for v in g}) for k in [0,1]]
for c in [1, 1000000-1]:
    f = [(v[0]+c*bisect.bisect_left(e[0],v[0]),v[1]+c*bisect.bisect_left(e[1],v[1])) for v in g]
    print(sum([abs(u[k]-v[k]) for u,v in combinations(f,2) for k in [0,1]])) # 10228230, 447073334102