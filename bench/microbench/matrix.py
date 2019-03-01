from numpy import *
from numpy.random import rand, randn
from numpy.linalg import matrix_power

def matrix_multiply(n):
    a = rand(n,n)
    b = rand(n,n)
    return dot(a,b)


def matrix_stats(t):
    n = 5
    v = zeros(t)
    w = zeros(t)

    for i in range(t):
        a = rand(n,n)
        b = rand(n,n)
        c = rand(n,n)
        d = rand(n,n) 

        p = concatenate((a,b,c,d), axis=1)
        q = concatenate((concatenate((a,b),axis=1), concatenate((c,d), axis=1)), axis=0)

        v[i] = trace(matrix_power(dot(p.T,p),4))
        w[i] = trace(matrix_power(dot(q.T,q),4))

    return (std(v)/mean(v), std(w)/mean(w))


def bench():
    import time
    trials=1000
    start1 = time.time()
    for a in range(trials):
        c=matrix_multiply(1000)
    stop1 = time.time()

    start2 = time.time()
    for b in range(trials):
        (d,e)=matrix_stats(1000)
    stop2 = time.time()
    return [(stop1 - start1), (stop2 - start2)]

if __name__=="__main__":
    print(bench())
