# Zipped!

if __name__ == "__main__":

	n, x = input().split()

	scores = []
	for i in range(int(x)):
		scores.append(list(map(float, input().split())))

	print(*[round(sum(k)/int(x), 1) for k in zip(*scores)], sep='\n')


