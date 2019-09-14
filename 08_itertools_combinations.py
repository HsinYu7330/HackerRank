# itertools.combinations()

from itertools import combinations

if __name__ == "__main__":

	s, n = input().split(' ')

	for i in range(int(n)):
		C = list(combinations(sorted(s), i+1))
		print(*[''.join(x) for x in C], sep='\n')

