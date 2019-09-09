# Collections.namedtuple()

from collections import namedtuple

if __name__ == '__main__':

    n = int(input())
    stu = namedtuple('stu', input())

    marks = []
    for i in range(n):
        marks.append(int(stu(*input().split()).MARKS))
    print('%.2f'%(sum(marks)/ n))