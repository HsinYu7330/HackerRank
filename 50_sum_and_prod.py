# Sum and Prod

import numpy as np

if __name__ == "__main__":

	n, m = map(int, input().split(' '))

	arr = []
	for i in range(n):
		arr.append(list(map(int, input().split(' '))))
	arr = np.array(arr)
	print(np.prod(np.sum(arr, axis=0), axis=0))
