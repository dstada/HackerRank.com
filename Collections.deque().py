from collections import deque
d = deque()
for i in range(int(input())):
    cn = input().split()
    if len(cn) == 2:
        cmd_string = "d."+cn[0]+"("+cn[1]+")"
        print(cmd_string)
    else:
        cmd_string = "d." + cn[0]+"()"
        print(cmd_string)
    eval(cmd_string)
print(*d)





"""
https://www.hackerrank.com/challenges/py-collections-deque/problem
Perform append, pop, popleft and appendleft methods on an empty deque d.
Input:
6
append 1
append 2
append 3
appendleft 4
pop
popleft
Output:
1 2

>>> from collections import deque
>>> d = deque()
>>> d.append(1)
>>> print d
deque([1])
>>> d.appendleft(2)
>>> print d
>>> d.pop()
"""