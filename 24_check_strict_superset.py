# Check Strict Superset

if __name__ == "__main__":

	a = set(map(int, input().split()))
	n = int(input())
	results = []
	for i in range(n):
		results.append(a.issuperset(set(map(int, input().split()))))

	print(all(results))

