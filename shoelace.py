# https://en.wikipedia.org/wiki/Shoelace_formula

P = [1+6j, 3+1j, 7+2j, 4+4j, 8+5j] # 16.5
# P= [0,6,6+6j,6j] # 36 (=6x6)
s = 0
for p0,p1 in zip(P,P[1:] + [P[0]]):
#     det = p0.real * p1.imag - p0.imag * p1.real
    det = - (p0*p1.conjugate()).imag
    s += det
print(s/2)