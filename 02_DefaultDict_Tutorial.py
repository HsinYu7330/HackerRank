# DefaultDict Tutorial

from collections import defaultdict

if __name__ == '__main__':

	n, m = map(int, input().split(' '))

	d = defaultdict(list)
	for i in range(n):
		d[input()].append(str(i+1))

	for i in range(m):
		g = input()
		if g in d:
			print(' '.join(d[g]))
		else:
			print(-1)