l = [list(map(int,b)) for b in [q.split(' ') for q in open('2023_09.txt').read().split('\n')]]

def down(d):
    if not any(d): return [0,0]
    else:
        w = down([u-v for v,u in zip(d[:-1],d[1:])])
        return [d[-1] + w[0], d[0] - w[1]]

[print(sum([v[i] for v in [down(v) for v in l]])) for i in range(2)] # 2174807968, 1208