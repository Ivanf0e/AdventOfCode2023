import re
from math import prod

f,p = open('2023_19.txt').read().split('\n\n')
R = {x: [s.split(':') if ':' in s else ['1', s] for s in r.split(',')]
        for x,r in re.findall('^(\w*)\{(.*?)\}', f, re.M)}

s1, s2, S = [], [], [('in', dict(zip('xmas', [(1, 4000)] * 4)))]
for r in re.findall('^\{(.*?)\}', p, re.M):
    c,i = 'in', 0
    x,m,a,s = (int(s[2:]) for s in re.split(',',r))
    while c not in 'AR':
        r,c1 = R[c][i]
        if eval(r):
            c,i = c1, 0
        else: i += 1
    s1.append( (x+m+a+s) * (c == 'A'))
    
while S:
    c, xmas = S.pop()
    if c == 'A': s2.append(prod(x[1] - x[0] + 1 for x in xmas.values()))
    elif c != 'R':
        for r,c1 in R[c][:-1]: # split all but last rule
            v,o,n = re.split('(<|>)',r) # () outputs the split-symbol too
            a = xmas.get(v)
            if o =='>':
                xmas[v] = (1 + max(a[0],int(n)), a[1]) # split off
                S.append((c1, xmas.copy()))
                xmas[v] = (a[0], min(a[1],int(n))) # new range for this test
            elif o =='<': # gave up to combine making less then 4 different ranges
                xmas[v] = (a[0], min(a[1], int(n)) - 1) # split off
                S.append((c1, xmas.copy()))
                xmas[v] = (max(a[0],int(n)),a[1])
        S.append((R[c][-1][1], xmas.copy())) # at last rule no split

print(sum(s1), sum(s2)) # 420739, 130251901420382