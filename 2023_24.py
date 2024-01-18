import re
from itertools import combinations
import numpy as np

data = [list(map(int,re.split(r'@|,',v))) for v in open('2023_24.txt').read().split('\n')]
l,u,c1,n = 200000000000000, 400000000000000, 0, len(data)

for a,b in combinations(data, 2):
#     a[i] + a[i+3] * t[0] = b[i] + b[i+3] * t[1] for i in [0,1]
    try:
        t = np.linalg.solve(np.array([[-a[3], b[3]],[-a[4], b[4]]]), np.array([a[0] - b[0], a[1] - b[1]]))
        if t[0] >= 0 and t[1] >= 0:
            x,y = a[0] + a[3] * t[0], a[1] + a[4] * t[0]
            if x >= l and x<=u and y >=l and y <= u: c1 += 1
#             else: print(x,y,'outside')
#         else: print(x,y,'past')
    except: pass #print('parallel',a[3:],b[3:],np.array([[-a[3], b[3]],[-a[4], b[4]]]))
print(c1) # 26657

# 6 + n unknowns in 3n equations, so only need n=3 for deterministic system
# pi + ti vi = p + ti v -> ti (v x vi) = (p - pi) x v
# ti (vi x v) = (pi - p) x vi -> ti (v x vi) = (p - pi) x vi
# 0 = (p-pi) x (v-vi) -> += (p-pj) x (v-vj)
# = (p-pi-p+pj) x (v-vi-v+vj) + (p-pi)x(vj-v) + (p-pj)x(vi-v)
# (since axb + cxd = (a-c)x(b-d) + axd + cxb
# *p --> (pj-pi)x(vj-vi)p = (p-pi)x(vj-v)p + ... = p x(p-pi) (vj-v) + ...
# = p x pi (vj-v) +  pj x p (v-vi)
# = (p(vj-v)-pj)x(pi-p(v-vi)) + pxp(v-vi) + pj x pi (vj-v)
# -=(p(vi-v)-pi)x(pj-p(v-vj)) + 0         + pj x pi (vi-v)
# (changing i and j which does not change left hand side. pxp=0)
# = pj x pi (vj-vi)
# --> (vi - vj) x (pi - pj) p = (vi - vj) pi x pj
# inspired by https://www.reddit.com/r/adventofcode/comments/18pum3b/comment/kge0mw5/?context=3

A = [[(a[4]-b[4]) * (a[2]-b[2]) - (a[5]-b[5]) * (a[1]-b[1]),
      (a[5]-b[5]) * (a[0]-b[0]) - (a[3]-b[3]) * (a[2]-b[2]),
      (a[3]-b[3]) * (a[1]-b[1]) - (a[4]-b[4]) * (a[0]-b[0])]
     for a,b in combinations(data[:3], 2)]
b = [(a[5]-b[5]) * (a[0]*b[1] - a[1]*b[0]) +
     (a[4]-b[4]) * (a[2]*b[0] - a[0]*b[2]) +
     (a[3]-b[3]) * (a[1]*b[2] - a[2]*b[1])
     for a,b in combinations(data[:3], 2)]
# interger values too large for linalg.solve
print(sum(np.dot(np.linalg.inv(A),b))) # 828418331313365