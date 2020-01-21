# Shape and Reshape

import numpy 

if __name__ == "__main__":

	arr = numpy.array(input().strip().split(' '), int)
	print(numpy.reshape(arr, (3, 3)))