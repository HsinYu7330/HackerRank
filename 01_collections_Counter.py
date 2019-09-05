# collections.Counter()

from collections import Counter

if __name__ == '__main__':

	shoes_cnt = input()
	shoes_size = Counter(input().split(' '))
	cust_cnt = int(input())

	total = []
	for i in range(cust_cnt):
		size, amount = list(map(int, input().split(' ')))

		if shoes_size[str(size)] > 0:
			total += [amount]
			shoes_size[str(size)] -= 1

	print(sum(total))






