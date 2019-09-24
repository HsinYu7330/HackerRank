# Set.discard(), .remove() & .pop()

if __name__ == '__main__':

	n = int(input())
	s = set(map(int, input().split()))
	N = int(input())

	for i in range(N):
		ele = input().split()
		if ele[0] == 'pop':
			s.pop()
		elif ele[0] == 'remove':
			s.remove(int(ele[1]))
		else:
			s.discard(int(ele[1]))

	print(sum(s))

