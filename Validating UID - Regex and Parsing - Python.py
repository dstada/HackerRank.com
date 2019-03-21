import re

for _ in range(int(input())):
    if bool(re.match(r'^[7-9]{1}\d{9}$', input())) is True:
        print("Valid")
    else:
        print("Invalid")





"""
Input:
2
B1CD102354
B1CDEF2354

Output:
Invalid
Valid

https://www.hackerrank.com/challenges/validating-uid/problem

A valid UID must follow the rules below:

It must contain at least  uppercase English alphabet characters.
It must contain at least  digits (0 -9 ).
It should only contain alphanumeric characters (a -z , A -Z  & 0 -9 ).
No character should repeat.
There must be exactly  characters in a valid UID.
"""