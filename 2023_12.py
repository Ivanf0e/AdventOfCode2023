cache = {} # store data, because recursive branch searching will result a lot of duplicates

def cnt(c, n):
    # stop the search if either string or instructions empty
    # and only at end we know if branch was valid, ie return 1
    if c == "": # if string empty, only valid if no instruction left
        return 1 if n == () else 0
    elif n == (): # if no instruction left, invalid if # left
        return 0 if '#' in c else 1
    
    # if c,n pair already obtained, load from memory
    if (k:=(c, n)) in cache:
        return cache[k]
    
    # split the search into no-block branch and a block branch. 
    r = 0 # track possible branches in r
     
    if c[0] in '.?': # try no-block, ie check rest of string
        r += cnt(c[1:], n)
    
    if c[0] in '#?': # block: only if sufficient string left and no adjacent blocks (either upto end or no next block)
        if n[0] <= len(c) and '.' not in c[:n[0]] and (n[0] == len(c) or c[n[0]] != '#'):
            r += cnt(c[n[0] + 1:], n[1:]) # +1 to remove the gap for next block, and remove first instruction
        else: # if the block does not fits, stop this branch. ie r += 0
            pass
        
    cache[k] = r
    return r

s0, s1 = 0, 0

for l in open('2023_12.txt').read().split('\n'):
    c, n = l.split(' '); n = eval(n)
    s0 += cnt(c, n)
    s1 += cnt('?'.join([c]*5), n*5)
print(s0, s1) # 7670, 157383940585037