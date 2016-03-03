import numpy as np
import sys

count = 0
v = 0
M = np.matrix([[]])

def kronecker(n):
    a = np.matrix([[1, 1], [0, 1]])
    if n == 1:
        return a
    return np.kron(a, kronecker(n - 1))

def gen(n):
    global count
    count = 1

    Max_Dim = pow(2,n)
    f = []
    for i in xrange(Max_Dim):
        f.append(0)

    if v: print "H: ", f, "i: ", pow(2,n) - 1, "count: ", count
    for i in reversed(xrange(0, Max_Dim)):
        gen_i(f, i, n)

    print "D" + str(n) + ": " + str(count)

def gen_i(G, i, n):
    global M
    H = []
    Max_Dim = pow(2,n)
    for p in xrange(Max_Dim):
        H.append(0)

    M_i = M[i]
    for k in xrange(Max_Dim):
        H[k] = G[k] or M_i[k]


    global count
    count += 1
    if v: print "H: ", H, "i: ", i, "count: ", count
    for j in reversed(xrange(i+1, Max_Dim)):
        if v: print "\tH: ", H, "i: ", i, "j: ", j
        if H[j] == 0:
            if v: print "--"
            gen_i(H, j, n)


if __name__ == '__main__':
    n = int(sys.argv[1])
    if len(sys.argv) == 3:
        if sys.argv[2] == '-v':
            v = 1
    M = kronecker(n).tolist()
    for row in M:
        if v: print row
    if v: print "\n"
    gen(n)

