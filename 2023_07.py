l0 = [[v[0:5], int(v[6:])] for v in open('2023_07.txt').read().split('\n')]
p1 = False

sc, sk = [[] for j in range(7)], [[] for j in range(7)]
for j,(l,_) in enumerate(l0):
    if p1:
        h = l.replace('J','X')
        sh = sum(['J23456789TXQKA'.index(i)*16**(4-j) for j,i in enumerate(h)])
        n = 5
    else:
        sh = sum(['J23456789TXQKA'.index(i)*16**(4-j) for j,i in enumerate(l)])
        h = l.replace('J','')
        dj = 5 - (n:=len(h))
    if dj >=4: s = 6
    else:
        s = 0
        while n > 1:
            h = h.replace(h[0],'')
            d = n - (n:=len(h))
            if d == 5: s=6; break
            elif d == 4: s=5; break
            elif d == 3: s+=3
            elif d == 2: s+=1
        if dj == 1:
            if s == 0: s = 1
            elif s == 1: s = 3
            elif s == 2: s = 4
            elif s == 3: s = 5
            elif s == 5: s = 6
        elif dj == 2:
            if s == 0: s = 3
            elif s == 1: s = 5
            elif s == 3: s = 6
        elif dj == 3:
            if s == 0: s = 5
            elif s == 1: s = 6
    sc[s].append(j);    sk[s].append(sh)

ln = sum([[l0[t[v]][1] for v in sorted(range(len(s)), key=lambda k: s[k])] for s,t in zip(sk,sc)],[])
print(sum([l*(j+1) for j,l in enumerate(ln)])) # 251106089, 249620106