# Mean, Var, and Std

import numpy
numpy.set_printoptions(legacy='1.13')

if __name__ == "__main__":

	n, m = map(int, input().split())
	arr = numpy.array([list(map(int, input().split())) for i in range(n)])
	print(numpy.mean(arr, axis=1))
	print(numpy.var(arr, axis=0))
	print(numpy.std(arr, axis=None))

