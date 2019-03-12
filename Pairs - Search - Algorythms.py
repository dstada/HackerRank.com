"""
You will be given an array of integers and a target value. Determine the number of pairs of array elements
that have a difference equal to a target value.

Dick Stada - March 2019
"""
import math
import os
import random
import re
import sys


def pairs(k, arr):      # k is target value
    pairs = 0
    for getal in arr:
        if getal + k in arr:
            pairs += 1
    return pairs


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    arr = list(map(int, input().rstrip().split()))
    result = pairs(k, arr)
    print(result)



"""https://www.hackerrank.com/challenges/pairs/problem

input:
5 2  
1 5 3 4 2

output:
3

def pairs(k, arr):      # k is target value
    # sort arr:
    arr = sorted(arr)
    pairs = 0
    for i in range(len(arr) - 1):
        for j in range(1 + i, len(arr)):
            if arr[j] - arr[i] == k:
                pairs += 1
                break
    return pairs

"""