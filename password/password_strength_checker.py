#PROGRAM TO CHECK STRENGTH OF PASSWORD

import re

print("Enter Password To Check Strength")
passwd = str(input())
len_pass = len(passwd)
pattern = r'[0-9]'
len_num = len(re.findall(pattern,passwd))
pattern = r'[\!\@\#\$\%\&\*\(\)]'
len_char = len(set(re.findall(pattern,passwd)))

def check(p,n,sc):
    if p >= 7:
        if n >= 2:
            if sc >= 2:
                return 'Strong'
            else:
                return 'Weak'
        else:
            return 'Weak'
    else:
        return 'Weak'

result = check(len_pass,len_num,len_char)
print("Your Password " + passwd + " is :")
print(result)
