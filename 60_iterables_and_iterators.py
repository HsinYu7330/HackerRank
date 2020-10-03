from itertools import combinations

def find_combination_contain_a(n: int, s: str, k: int) -> float:
    """Find how much percentage of combinations contain "a"

    Returns:
        percentage of combinations contain "a" in Float
    
    Args:
        n: length of list
        s: space-separated lowercase English letters, the elements of the list
        k: the number of indices to be selected
    """
    comb = ['a' in x for x in combinations(s.split(' '), k)]
    return round(sum(comb)/len(comb), 3)

if __name__ == '__main__':
    n = int(input())
    s = str(input())
    k = int(input())
    print(find_combination_contain_a(n, s, k))