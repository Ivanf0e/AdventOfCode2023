G = {i + j*1j: c for j,r in enumerate(open('2023_23.txt')) for i,c in enumerate(r.strip()) if c != '#'}
E = {p: [p+d for d in (1,-1,1j,-1j) if p+d in G] for p in G}

def collapse(E, G, part1):
    N = {p: [] for p,v in E.items() if len(v)>2 or p==[*G][0] or p==[*G][-1]}
    for c in N:
        U = [(c,0)]
        V = set()
        while U:
            p, d = U.pop()
            if p in V: continue
            V.add(p)
            for v in [1,1j,-1,-1j]:
                if (x:= p+v) in G and x not in V:
                    if not part1 or G[x] == '.' or (G[x] == '>' and v != -1) or (G[x] == 'v' and v != -1j):
                        if x in N:
                            N[c].append((x,d+1))
                        else:
                            U.append((x, d+1))
    return N

def dfs(g, c, d=0, V=set()):
    if c == [*G][-1]: return d
    best = 0
    V.add(c)
    
    for n, dn in g[c]:
        if n in V:
            continue
        best = max(best, dfs(g, n, d + dn))
    V.remove(c)
    return best


print(dfs(collapse(E, G, True) ,[*G][0])) # 2406
print(dfs(collapse(E, G, False) ,[*G][0])) # 6630