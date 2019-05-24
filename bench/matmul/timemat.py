def timemat(n,m):
	import numpy
	import time

	t = time.time()
	X = numpy.random.rand(m, n+1)
	Y = numpy.random.rand(m, 1)
	theta = numpy.linalg.inv(X.T @ X) @ X.T @ Y

	return time.time() -t

if __name__ == '__main__':
	import sys
	n = 1000
	m = 100

	if len(sys.argv) > 2:
		n = int(sys.argv[1])
		m = int(sys.argv[2])

	print(timemat(n,m))
