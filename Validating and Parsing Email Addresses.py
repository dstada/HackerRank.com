import email.utils
import re

print(email.utils.parseaddr('DOSHI <DOSHI@hackerrank.com>'))
print(email.utils.formataddr(('DOSHI', 'DOSHI@hackerrank.com')))

for _ in range(int(input())):
    inptt = input()
    # print(inptt)
    inpt = email.utils.parseaddr(inptt)
    # print(inpt[0])
    # print(inpt[1])
    if bool(re.match(r'^[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}$', inpt[1])) is True:
        # in plaats van (\w|-|.|_) kan [\w-._] ook
        print(inptt)

"""
2
DEXTER <dexter@hotmail.com>
VIRUS <virus!@variable.:p>
Sample Output

DEXTER <dexter@hotmail.com>
"""