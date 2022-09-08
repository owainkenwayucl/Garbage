import sys
import time
import math
import random

def integralpi(n, m):
	numsamples = n*m
	totalsum = 0
	step = 1.0/numsamples

	p = step * sum(4.0/(1.0 + ((i + 0.5) * (i + 0.5) * step * step)) for i in range(numsamples))

	return p, abs(p - math.pi)
	

def montecarlopi(n, m):
	numsamples = n*m

	count = 0
	for a in range(numsamples):
		x = random.random()
		y = random.random()
		if ((x*x + y*y) <= 1):
			count += 1

	p = 4*count/numsamples
	return p, abs(p - math.pi)


def gridpi(n, m):
	p = math.pi
	xstep = 1.0/n
	ystep = 1.0/m

	count = 0
	for a in range(n):
		for b in range(m):
			x = 0.0 + (a * xstep)
			y = 0.0 + (b * ystep)
			if ((x*x + y*y) <= 1):
				count += 1

	p = 4*count/(n*m)


	return p, abs(p - math.pi)


def timefunc(function, n, m):
	start = time.time()
	p, err = function(n,m)
	stop = time.time()
	return (stop - start), p, err

def bench(lower, step, upper):
	current = lower

	print("Samples, Integral time, Integral error, Monte Carlo time, Monte Carlo error, Grid time, Grid error")
	while (current < upper):
		dim = math.floor(math.sqrt(current))
		real = dim * dim
		it, ip, ie = timefunc(integralpi, dim, dim)
		mt, mp, me = timefunc(montecarlopi, dim, dim)
		gt, gp, ge = timefunc(gridpi, dim, dim)
		print(str(real) + ", " + str(it) + ", " + str(ie) + ", " + str(mt) + ", " + str(me) + ", " + str(gt) + ", " + str(ge) + ", " )

		current += step

if __name__ == '__main__':
	begin = 1000
	stop = 10000
	step = 100

	if len(sys.argv) > 1:
		begin = int(sys.argv[1])
	if len(sys.argv) > 2:
		step = int(sys.argv[2])
	if len(sys.argv) > 3:
		stop = int(sys.argv[3])

	bench(begin, step, stop)
	
