# Min and Max

if __name__ == "__main__":

	n, m = map(int, input().split())
	min_ele = []
	for i in range(n):
		x1, x2 = map(int, input().split())
		min_ele.append(min([x1, x2]))
	
	print(max(min_ele))





