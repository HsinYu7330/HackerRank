# Validating and Parsing Email Addresses

import email.utils
import re

if __name__ == "__main__":

    n = int(input())

    for i in range(n):
        name, mail = email.utils.parseaddr(input())
        
        if bool(re.match(r'[A-Za-z](\w|\.|-|_)+@[A-Za-z]+\.[A-Za-z]{1,3}$', mail)):
            print(email.utils.formataddr((name, mail)))