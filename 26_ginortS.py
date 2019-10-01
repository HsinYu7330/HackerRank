# ginortS

if __name__ == "__main__":

	s = input()
	lower = sorted([x for x in s if x.islower()])
	upper = sorted([x for x in s if x.isupper()])
	even = sorted([x for x in s if (x.isdigit()) and (int(x)%2 == 0)])
	odd =  sorted([x for x in s if (x.isdigit()) and (int(x)%2 != 0)])

	print(''.join(lower+upper+odd+even))