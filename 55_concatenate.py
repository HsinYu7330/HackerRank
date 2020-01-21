# Concatenate

import numpy

if __name__ == "__main__":

	n, m, p = map(int, input().split(' '))
	arr = []
	for i in range(n+m):
		arr.append(list(map(int, input().split(' '))))
	print(numpy.array(arr))
