import re

l0,l1=[],[]
ints = ['one','two','three','four','five','six','seven','eight','nine']

for line in open('2023_01.txt'):
    x = re.findall(r'(\d)', line)
    l0.append(int(x[0] + x[-1]))

    for i, n in enumerate(ints):
        line = line.replace(n, n + str(i+1) + n)
    x = re.findall(r'(\d)', line)
    l1.append(int(x[0] + x[-1]))

print(sum(l0), sum(l1)) # 54644, 53348