m = {i + j*1j: c for j,r in enumerate(open('2023_16.txt')) for i,c in enumerate(r.strip())}
R = [] # number of rays for different start positions
xrange, yrange = range(int([*m][-1].real)+1), range(int([*m][-1].imag)+1)
rot = lambda v, u: u * (v.imag + 1j* v.real) # rotate velocities

for s in [(x+1j*y,u) for y in yrange for x,u in [(0,1),(xrange[-1], -1)]] + [(x+1j*y,1j) for y,v in [(0,1),(yrange[-1], -1)] for x in xrange]:
    V = [] # visited rays. as list, because no look-up and nice to see the order
    U = {s} # unvisited states for position and velocity
    T = {x+1j*y for y in yrange for x in [xrange[0]-1,xrange[-1]+1]} | {(x+1j*y) for y in [yrange[0]-1,yrange[-1]+1] for x in xrange} # termination points

    while U:
        pos, vel = U.pop() # unpack state
        if pos in T: continue # termination point so stop

        V += [pos] # add ray to points
        c = m[pos]
        
        if (c=='-' and vel.imag) or (c=='|' and vel.real): # splitter
            vel = vel.imag + 1j* vel.real #-vel/1j #v, u = u, v
            U.add((pos - vel, -vel)) # update position
            T.add(pos) # terminate at splitters, since do not have to visited twice
        elif c == '\\': # change direction
            vel = vel.imag + 1j* vel.real #-vel/1j #v, u = u, v 
        elif c =='/':
            vel = -vel.imag - 1j* vel.real #vel/1j #v, u = -u, -v
        # else: pass # continue straight
        
        U.add((pos + vel, vel)) # update position
        
    R.append(len(set(V)))        
    
print(R[0], max(R)) # 6883, 7228

# plotting
# for y,x in V:
#     m[y][x] = '#'
# [print(''.join(v)) for v in m]