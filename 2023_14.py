e = open('2023_14.txt').read().split()
p = len(e) # starting points of top row

def roll(w): # rolls everything to left
    a = []
    for r in [[v[j] for v in w] for j in range(p)]: # transpose first
        pl,s = p, ''
        for j,v in enumerate(r):
            if v == 'O':
                s += 'O'
            elif v == '#':
                s += '.'*(j-len(s)) + '#'
        s += '.'*(j-len(s)+1) # trail with dots
        a += [s]
    return(a)
    
s1 = []    
for k in range(122):
    a = roll(e)
    if k == 0: print(sum([v.count('O')*(p-j) for j,v in enumerate([[v[j] for v in a] for j in range(p)])]))
    b = roll(a)
    c = roll(b[::-1])
    d = roll(c[::-1])
    e = [v[::-1] for v in reversed(d)] # put North up again
    s = sum([v.count('O')*(p-j) for j,v in enumerate(e)])
    if len(s1)>12 and s in s1: # some number to prevent random start repeats
        if (jj := s1[::-1].index(s)) > 3:
            i = len(s1)-1-jj
            if all([s1[-1-j]==s1[i-1-j] for j in range(jj)]): # todo make repeat function
                print(s1[(len(s1)//(jj+1) -1 ) * (jj+1) + (1000000000-1)%(jj+1)]) # 106689
                break
    s1 += [s]