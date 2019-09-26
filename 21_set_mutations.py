# Set Mutations

if __name__ == '__main__':

	N = input()
	s = set(map(int, input().split()))
	operation_n = int(input())

	for i in range(operation_n):
		o, n = input().split()
		a = set(map(int, input().split()))
		if o == 'intersection_update':
			s.intersection_update(a)
		elif o == 'update':
			s.update(a)
		elif o == 'symmetric_difference_update':
			s.symmetric_difference_update(a)
		else:
			s.difference_update(a)

	print(sum(s))

