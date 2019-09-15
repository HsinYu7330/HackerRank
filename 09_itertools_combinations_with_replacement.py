# itertools.combinations_with_replacement()

from itertools import combinations_with_replacement

if __name__ == '__main__':

	s, n = input().split(' ')

	C = list(combinations_with_replacement(sorted(s), int(n)))
	print(*[''.join(x) for x in C], sep='\n')