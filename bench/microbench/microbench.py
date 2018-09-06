def pisum():
	s = 0.0
	for j in range(1,501):
		s = 0.0
		for k in range(1, 10001):
			s += 1.0/(k*k)
	return s

def bench():
	import time
	start = time.time()
	pisum()
	stop = time.time()
	return (stop - start)

if __name__=="__main__":
	print(bench())
