# Inner and Outer

import numpy

if __name__ == "__main__":
	
	A = numpy.array(list(map(int, input().split())))
	B = numpy.array(list(map(int, input().split())))
	print(numpy.inner(A, B))
	print(numpy.outer(A, B))

