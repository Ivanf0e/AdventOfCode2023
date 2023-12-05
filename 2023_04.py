import re

l0=[]
for line in open('2023_04.txt'):
    d = [map(int,re.findall(r'\d+', v)) for v in re.split(r"[:|]", line)]
    l0.append(len(set(d[1]) & set(d[2]))) # number of wins = intersect of lists

l1 = [1] * (n:=len(l0)) # start with 1 copy per card
for j,w in enumerate(l0):
    for i in range(w): # win copies of cards = point of current card
        l1[j+i+1] += l1[j] # repeat for all number of current card

print(sum([2**(v-1) if v>0 else 0 for v in l0]), sum(l1)) # 21213, 8549735