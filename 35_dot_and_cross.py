# Dot and Cross

import numpy

if __name__ == "__main__":

	n = int(input())
	A = numpy.array([list(map(int, input().split())) for i in range(n)])
	B = numpy.array([list(map(int, input().split())) for i in range(n)])
	print(numpy.matmul(A, B))
