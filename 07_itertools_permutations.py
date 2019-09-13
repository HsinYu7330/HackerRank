# itertools.permutations()

from itertools import permutations

if __name__ == "__main__":

	s, k = input().split(' ')
	P = list(permutations(s, int(k)))
	print(*sorted([''.join(x) for x in P]), sep='\n')

