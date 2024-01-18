import re
from math import prod

d = dict()
for r in [re.split(' -> |, ',c) for c in open('2023_20.txt').read().split('\n')]:
    d[r[0][1:]] = [r[0][0], 0 if r[0][0] == '%' else 1, r[1:], []]

for k,v in d.items(): # check all inputs for &
    for u in v[2]:
        if u in d and d[u][0] == '&':
            d[u][3].append(k)

pc, s2, k, go = [0,0], {v:0 for v in d['cs'][3]}, 0, True

while go:
    if k == 1000: s1 = pc.copy()
    k += 1
    U = [(0, 'roadcaster')] #(0,v) for v in d['roadcaster'][2]]

    while U:
        p,u = U.pop(0)
        pc[p] += 1
        if u not in d: continue
        elif d[u][0] == 'b':
            d[u][1] = 0    
        elif d[u][0] == '%' and not p:
            d[u][1] = 1 - d[u][1]
        elif d[u][0] == '&':
            d[u][1] = 1 - all([d[v][1] for v in d[u][3]])
            if u in s2.keys() and d[u][1]:
                s2[u] = k
                go = not all(s2.values())
        else: continue
        
        U += [(d[u][1], v) for v in d[u][2]]

print(prod(s1), prod(s2.values())) # 703315117, 230402300925361