# Detect Floating Point Number

import re

for i in range(int(input())):
	print(bool(re.match(r"^[+-]?\d*\.+\d*$", str(input()))))

# Example
s = '4.0O0'
print(bool(re.match(r"^[+-]?\d*\.+\d*$", s)))