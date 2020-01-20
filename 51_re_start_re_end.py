# Re.start() & Re.end()

if __name__ == "__main__":

	s = input()
	k = input()

	if k in s:
		ix = 0
		while k in s[ix:]:
			m = re.search(r'%s'%(k), s[ix:])
			print('(%d, %d)'%(m.start()+ix, m.end()+ix-1))
			ix += m.start()+1
	else:
		print('(%d, %d)'%(-1, -1))