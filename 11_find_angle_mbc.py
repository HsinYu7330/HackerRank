# Find Angle MBC

import math

if __name__ == '__main__':

	ab = int(input())
	bc = int(input())
	angle_c = int(round(math.degrees(math.atan(ab/bc))))

	print('%s%s'%(angle_c, chr(176)))




