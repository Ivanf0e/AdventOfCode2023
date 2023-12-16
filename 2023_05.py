import re

# split on double newlines and find maps as integers
m = [list(map(int, re.findall(r'\d+', b))) for b in open('2023_05.txt').read().split('\n\n')]

def a2b(s,n):
    for i,d,t in (zip(n[1::3],n[2::3],n[::3])):
        if s>=i and s<i+d:
            return s-i+t
    return s        

def a2c(sq,n):
    s = sq.pop(0)
    for i,d,t in (zip(n[1::3],n[2::3],n[::3])):
        if s[0]>=i and s[0]<i+d: 
            if  s[1]<i+d:		# start & end in range
                return [s[0]-i+t, s[1]-i+t]
            else:		# start in range, end not: split
                sq.append([i+d,s[1]])
                return [s[0]-i+t,t+d-1]
        elif s[1]>=i and s[1]<i+d: # start not in range, end is: split
            sq.append([s[0],i-1])      
            return [t, s[1]-i+t]
    return s # start & end both not in range

l0 = [v for v in m[0]] # m[0] holds seeds
l1 = [[v[0],v[0]+v[1]] for v in zip(m[0][::2],m[0][1::2])] # m[0] holds start and range
for m1 in m[1:]:
    l0 = [a2b(v,m1) for v in l0] # update number based on map
    sq, l1 = [v for v in l1], []
    while(sq):   
        r = a2c(sq,m1)
        l1.append(r)

print(min(l0), min([v[0]for v in l1])) # 218513636, 81956384