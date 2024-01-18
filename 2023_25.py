import re
from collections import defaultdict

D = defaultdict(lambda:set())

for v in [re.split(r': | ',v) for v in open('2023_25a.txt').read().split('\n')]:
    for b in v[1:]: D[v[0]].add(b); D[b].add(v[0])

S = set(D) # oppertunistic: remove most external neighbours without guarantee on success
count = lambda v: len(D[v] - S) # count how many neighbours are not in S

while sum(map(count, S)) != 3: # stop when exactly 3 neighbours outside S
    S.remove(max(S, key=count)) # remove node with most neighbours not in S

print((len(D)-len(S)) * len(S)) # 548960