# Polar Coordinates

from cmath import phase
import re

if __name__ == '__main__':

	x, y = [int(d) for d in re.findall(r'-?\d+', input())]
	print(abs(complex(x, y)))
	print(phase(complex(x, y)))

