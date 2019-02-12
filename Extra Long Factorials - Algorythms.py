import math
import os
import random
import re
import sys


def extraLongFactorials(n):
    return math.factorial(n)


# Also possible:
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)


if __name__ == '__main__':
    n = int(input())

    print(extraLongFactorials(n))

"""
https://www.hackerrank.com/challenges/extra-long-factorials/problem
"""