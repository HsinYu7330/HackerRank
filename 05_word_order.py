# Word Order

from collections import OrderedDict

if __name__ == '__main__':
    n = int(input())

    word_dict = OrderedDict()
    for i in range(n):
        s = input()
        try:
            word_dict[s] += 1
        except:
            word_dict[s] = 1
    print(len(word_dict))
    print(*word_dict.values())
