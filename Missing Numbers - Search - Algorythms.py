import math
import os
import random
import re
import sys


# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    print(arr)
    print(brr)
    for number in arr:
        brr.remove(number)
    print(brr)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    m = int(input())
    brr = list(map(int, input().rstrip().split()))
    result = missingNumbers(arr, brr)
    print(result)

"""
https://www.hackerrank.com/challenges/missing-numbers/problem

input:
10
203 204 205 206 207 208 203 204 205 206
13
203 204 204 205 206 207 205 208 203 206 205 206 204

output:
204 205 206
"""