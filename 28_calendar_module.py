# Calendar Module

import calendar

if __name__ == '__main__':

	m, d, y = map(int, input().split())
	weekday = calendar.weekday(y, m, d)
	print(calendar.day_name[weekday].upper())

