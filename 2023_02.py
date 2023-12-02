import re
import math

l0,l1=[],[]
d = {'red':12,'green':13,'blue':14}
for j,line in enumerate(open('2023_02.txt')):
    m = {'red':0,'green':0,'blue':0}
    
    for n,k in [s.split() for s in re.split(r"[:,;]", line)[1:]]:
        m[k] = max(m[k], int(n))

    if any([k[1]>d[k[0]] for k in m.items()]):
        l0.append(j+1) # original with break when game was not possible, but shorter notation if combined with Part2

    l1.append(list(m.values()))

print((j+1)*(j+2)//2 - sum(l0), sum([math.prod(l) for l in l1])) #2795, 75561