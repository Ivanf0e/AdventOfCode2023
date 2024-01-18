import re
from copy import deepcopy

S = [list(map(int,re.findall("\d+", r))) for r in open('2023_22.txt').read().split('\n')]
ns = len(S); nx,ny,nz = [max([v[i] for v in S]) for i in [3,4,5]]

S.sort(key=lambda x: x[2]) # sort on lowest x values
F = [[(0,0) for _ in range(nx+1)] for _ in range(ny+1)] # floor with local height and last block (x before y for once)
P = [set() for _ in range(len(S)+1)] # all blocks supported by this block
C = deepcopy(P)

for j in range(len(S)):
    f = min([S[j][2]-F[x][y][0]-1 for x in range(S[j][0],S[j][3]+1) for y in range(S[j][1],S[j][4]+1)])
    S[j][2] -= f; S[j][5] -= f
    
    for x in range(S[j][0],S[j][3]+1):
        for y in range(S[j][1],S[j][4]+1):
            if F[x][y][0] + 1 == S[j][2]:
                P[j+1].add(F[x][y][1])
            F[x][y] = (S[j][5], j+1)

print(len(S) - len(set.union(*[v for v in P if len(v) == 1])) + 1) # 515 (+1 because we are subtracting the floor too)

for b in range(1, ns):
    Q = deepcopy(P)
    R = {b}
    while R: # probably more efficient to store branches and look-up
        r = R.pop()
        for j in range(r+1, len(P)):
            Q[j] -= {r}
            if not Q[j]:
                R.add(j)
                C[b].add(j)

print(sum(len(v) for v in C)) # 101541