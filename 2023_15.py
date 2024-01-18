from functools import reduce
data = open('2023_15.txt').read().strip().split(',')

char = lambda i, c: (i+ord(c)) * 17 % 256
hash = lambda s: reduce(char, s, 0)
print(sum(map(hash, data))) # 503487

b = [dict() for _ in range(256)] # 256 empty boxes
for l in data:
    match l.strip('-').split('='):
        case [p, f]: b[hash(p)][p] = int(f)
        case [p]: b[hash(p)].pop(p, 0) # if not box, pop returns 2nd parameter iso error

print(sum([i*j*f for i,k in enumerate(b, 1) # 261505
                 for j,f in enumerate(k.values(), 1)])) # dict keeps correct order from Python 3.6 onward