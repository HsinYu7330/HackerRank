# Re.findall() & Re.finditer()

import re

if __name__ == '__main__':

	v = 'aeiou' # vowels
	c = 'qwrtypsdfghjklzxcvbnm' # consonants
	m = re.findall(r'(?<=[%s])([%s]{2,})[%s]'%(c, v, c), input(), flags=re.I)
	print('\n'.join(m) if m else -1)

