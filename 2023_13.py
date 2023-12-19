s0, s1 = 0, 0

for l in open('2023_13.txt').read().split('\n\n'):
    w = l.split()
    ny,nx = len(w), len(w[0])
    for k in [0,1]:
        if k == 1: # in second run do same for transpose
            w = [[v[j] for v in w] for j in range(nx)]
            nx,ny = ny,nx
        M = [0 for _ in range(nx)] # amount of errors per row for a mirror image
        for r in w: # loop over rows, and only if error <=1
            for i in (q for q,e in enumerate([0 for _ in range(nx)]) if e <= 1 if q>0): # skip 0th, because mirror is arbitrary
                d = min(i,nx-i) # seeing length with mirror at i
                M[i] += d - sum([u==v for u,v in zip(r[i-d:i], r[i+d-1:i-1:-1])]) # count errors
        s0 += (100 if k else 1) * sum([j for j,e in enumerate(M) if e == 0]) # no errors allowed
        s1 += (100 if k else 1) * sum([j for j,e in enumerate(M) if e == 1]) # exactly 1 error required
    
print(s0, s1) # 43614, 36771