# No Idea!

if __name__ == '__main__':

	n, m = input().split()
	n_int = input().split()
	A = set(input().split())
	B = set(input().split())

	print(sum([(x in A) - (x in B) for x in n_int]))