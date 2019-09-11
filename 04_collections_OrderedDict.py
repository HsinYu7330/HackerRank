# Collections.OrderedDict()

from collections import OrderedDict

if __name__ == '__main__':
    n = int(input())
    
    transaction_dict = OrderedDict()
    for i in range(n):
        item = input().split(' ')
        item_name = ' '.join(item[:-1])
        item_price = int(item[-1])

        try:
            transaction_dict[item_name] += item_price
        except:
            transaction_dict[item_name] = item_price
        
    for name, net_price in transaction_dict.items():
        print(name, net_price)