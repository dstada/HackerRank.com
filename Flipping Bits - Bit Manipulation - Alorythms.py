"""
https://www.hackerrank.com/challenges/flipping-bits/problem

input:
2
4
123456

output:
4294967291
4294843839

input:
3
0
802743475
35601423

output:
4294967295
3492223820
4259365872
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flippingBits function below.
def flippingBits(n):


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()