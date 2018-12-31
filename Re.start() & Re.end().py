import re
s = input()
search_string = input()

if search_string in s:
    for i in range(len(s)):
        m = re.search(search_string, s[i:len(s)])
        if m:
            print("({}, {})".format(m.start() + i, m.end() - 1 + i))
            if m.end() + i == len(s):
                break
else:
    print("(-1, -1)")


"""
Sample Input
aaadaa
aa

Sample Output
(0, 1)  
(1, 2)
(4, 5)

import re
>>> m = re.search(r'\d+','1234')
>>> m.end()
4
>>> m.start()
0
"""