# The Captain's Room

from collections import Counter

if __name__ == '__main__':

	K = int(input())
	ele = list(map(int, input().split()))

	print([k for k, v in Counter(ele).items() if v == 1][0])

