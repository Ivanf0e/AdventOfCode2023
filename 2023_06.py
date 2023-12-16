import math
ts = [46  ,   85 ,    75  ,   82]
ds = [208 ,  1412  , 1257  , 1410]

ts.append(int(''.join([str(v) for v in ts])))
ds.append(int(''.join([str(v) for v in ds])))

# v*(t-v) > d  -->  v**2 - v*t + d > 0
# subtract it from the maximum of t-1 options 
l0 = [t-1 - 2*math.floor(t/2-math.sqrt((t/2)**2-d)) for t,d in zip(ts,ds)]
print(math.prod(l0[:-1]), l0[-1]) # 1108800, 36919753