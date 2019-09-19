# Symmetric Difference

if __name__ == "__main__":

	m = input()
	m_list = list(map(int, input().split(' ')))
	n = input()
	n_list = list(map(int, input().split(' ')))

	union_set = set(m_list).union(set(n_list))
	intersect_set = set(m_list).intersection(set(n_list))
	print(*sorted(union_set.difference(intersect_set)), sep='\n')

