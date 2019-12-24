# Map and Lambda Funcion

cube = lambda x: x**3

def fibonacci(n):

	if n == 0:
		return []
	elif n == 1:
		return [0]
	elif n == 2:
		return [0, 1]
	else:
		seq = [0, 1]
		while len(seq) != n:
			seq.append(sum(seq[-2:]))
		return seq

if __name__ == '__main__':
	n = int(input())
	print(list(map(cube, fibonacci(n))))


