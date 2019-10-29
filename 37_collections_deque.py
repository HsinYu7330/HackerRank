# Collections.deque()

from collections import deque

if __name__ == "__main__":

    n = int(input())
    d = deque()
    for i in range(n):
        mv = input().split()
        if mv[0] == 'append':
            d.append(int(mv[1]))
        if mv[0] == 'appendleft':
            d.appendleft(int(mv[1]))
        if mv[0] == 'pop':
            d.pop()
        if mv[0] == 'popleft':
            d.popleft()
    print(*d)