p1, a1, q1, a2 = 0, 0, 0, 0
D1 = {'U': -1j, 'D': 1j, 'L': -1, 'R': 1}
D2 = { 3 : -1j,  1 : 1j,  2 : -1,  0 : 1}

for d,s,rgb in [r.split(' ') for r in open('2023_18.txt').read().split('\n')]:
    p0, p1 = p1, p1 + D1[d] * (l:=int(s)) # find edge pairs
    a1 += l - (p0*p1.conjugate()).imag # area of edge + shoelace determinant
    
    q0, q1 = q1, q1 + D2[int(rgb[7],16)] *(l:=int(rgb[2:7],16))
    a2 += l - (q0*q1.conjugate()).imag

print(int(a1/2)+1, int(a2/2)+1) # 46394, 201398068194715