# Check Subset

if __name__ == '__main__':

	t = int(input())

	for i in range(t):
		n_a = int(input())
		a = set(map(int, input().split()))
		n_b = int(input())
		b = set(map(int, input().split()))
		
		print(a.issubset(b))


