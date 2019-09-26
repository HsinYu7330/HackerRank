# Set .intersection() Operation

if __name__ == '__main__':

	n = input()
	a = set(map(int, input().split()))
	m = input()
	b = set(map(int, input().split()))

	print(len(a & b))

	