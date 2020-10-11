from itertools import product
from typing import List

def maximize_list(inputlist: List[int], M: int):
    """make the equation s=(f(x1) + f(x2) + ... +f(xk))%M is maximized

    Returns:
        maximum value

    Args:
        inputlist: nested list from K lists
        M: M

    Example: 
        [5, 9 ,10]%1000 -> 206     
    """
    return max([sum(x)%M for x in list(product(*inputlist))])


if __name__ == '__main__':
    K, M = [int(x) for x in input().split(' ')]
    inputlist = []
    for i in range(K):
        inputlist.append([int(x)**2 for x in input().split(' ')[1:]])
    print(maximize_list(inputlist, M))


