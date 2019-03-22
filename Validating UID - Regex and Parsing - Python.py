import re

for _ in range(int(input())):
    if bool(re.match(r'^(?=(?:[a-z\d]*[A-Z]){2})(?=(?:.*\d){3})(?:([a-zA-Z\d])(?!.*\1)){10}$', input())) is True:
        print("Valid")
    else:
        print("Invalid")


"""
^: Start
(?=(?:[a-z\d]*[A-Z]){2}): Lookahead to assert that we have at least 2 uppercase alphabets
(?=(?:\D*\d){3}): Lookahead to assert that we have at least 3 digits
(?:([a-zA-Z\d])(?!.*\1)){10}: Match exact 10 alphanumeric characters. Negative lookahead is to assert that we don't have anything repeating anywhere.
$: End

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