from heapq import heappop, heappush # BFS but keep states sorted by heapq

G = {i + j*1j: int(c) for j,r in enumerate(open('2023_17.txt')) for i,c in enumerate(r.strip())}

for s0,s1 in [(1,4),(4,11)]:
    U = [(0,0,0,1), (0,0,0,1j)] # unvisted states of val, steps, pos, dir (val first because that is the sorter, when added 2nd because otherwise the will try to sort on position (which raises error for complex number)
    V = set() # visited pos and dir (revisitinf from same pos
    n = 0
    e = [*G][-1]

    while U:
        v, _, p, d = heappop(U) # heapq should give smallest value
        
        if p == e: print(v); break # 1039, 1201
        if (p,d) in V: continue 
        V.add((p,d))
        
        for s in range(s0,s1): # possible adjacents range 
            for di in [1j/d, -1j/d]: # in perpendicular dir
                if (pi:=p+di*s) in G:
                    vi = sum([G[p+di*j] for j in range(1,s+1)])
                    heappush(U, (v+vi, (n:=n+1), pi, di))