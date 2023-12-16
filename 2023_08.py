import math
from itertools import product, cycle

lr, m = open('2023_08.txt').read().split('\n\n') # split on double newline
m = {v[0:3]: [v[7:10], v[12:15]] for v in m.split('\n')} # put map in dict

def solve(p,q,n,f): # current position, solutions, desired solutions, solution criterium
    for j,d in enumerate(cycle(lr)):
        if f(p) and len(q:=q+[j])>n and not q[-1]%q[0]: return q[:-1] if n else q[0]
        # part 2: stop if solutions are looping, and then do not return last
        p = m[p][0] if d == 'L' else m[p][1]

print(solve('AAA', [], 0, lambda p: p == 'ZZZ')) # 15989

pe = [solve(p, [], 1, lambda x: x[2] == 'Z') for p in (v for v in m.keys() if v[2]=='A')]
print(min([math.lcm(*v) for v in product(*pe)])) # 13830919117339