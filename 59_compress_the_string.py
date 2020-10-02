from itertools import groupby
from typing import List

def compress_the_string(s: str) -> List[tuple]:
    """Compress the string

    Returns: 
        integers occurences in Tuple
    
    Args:
        s: integers between 0 and 9

    Example:
        '1222311' -> (1, 1) (3, 2) (1, 3) (2, 1)
    """
    return [(len(list(g)), int(k)) for k, g in groupby(s)]

if __name__ == '__main__':
    s = input()
    print(*compress_the_string(s))

