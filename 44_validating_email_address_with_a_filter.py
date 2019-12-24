# Validating Email Addresses With a Filter

import re 

def fun(s):

    if s.count('@') == 1 and s.count('.') == 1:
        username = s.split('@')[0]
        websitename = s.split('@')[1].split('.')[0]
        extension = s.split('@')[1].split('.')[1]

        condition1 = len(username) > 0 and bool(re.match(r'^[A-Za-z0-9_-]*$', username))
        condition2 = len(websitename) > 0 and bool(re.match(r'^[A-Za-z0-9]*$', websitename))
        condition3 = len(extension) <= 3

        if condition1 and condition2 and condition3:
            return True
        else:
            return False
    else:
        return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)

		


