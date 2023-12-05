z = open('2023_03.txt').read().splitlines() # reading files and adding dummies to ends
ny, nx = len(z), len(z[0])
z = [r+'.' for r in z] + ['.' * (nx+1)]

def nn(j, i0, i1):
    return [(j,i0),(j,i1-1),] + [(j+dj,x) for x in range(i0,i1) for dj in [-1,1]]

l0,l1,d=[],{}, False
for j,r in enumerate(z[:-1]):
    for i,c in enumerate(r): # look in middle line
        if c.isdigit():
            if not d: # start of digit
                d = True
                v = c
                i0 = i-1
            else:     # continue digit
                v += c
        elif d: # end of digit, look for nearest neigbours
            i1,u = i+1, int(v)
            yx = nn(j, i0, i1)  # nn coordinates
            zyx = [z[y][x] for y,x in yx] # nn characters
            if not all([c.isdigit() or c=='.' for c in zyx]):
                l0.append(u) # only add to part 1 if there is a symbol in nn
            if '*' in zyx: # if * in nn, add the number that touches it
                k = yx[zyx.index('*')]
                l1[k] = [u] if k not in l1 else l1[k] + [u]
            d = False

# for part 2, gear ratio is product of numbers touching * exactly 2x
print(sum(l0), sum([v[0]*v[1] for v in l1.values() if len(v)==2])) #507214, 72553319