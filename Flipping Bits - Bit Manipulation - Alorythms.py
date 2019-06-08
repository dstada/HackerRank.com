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

def dec_to_bin(i):
    if i == 0:
        return "0"
    s = ''
    while i:
        if i & 1 == 1:
            s = "1" + s
        else:
            s = "0" + s
        i //= 2
    return s

def bin_to_dec(bits):
    n = 0
    for b in bits:
        n = (n << 1) | (b == '1')
    return n

def flippingBits(n):
    bin = dec_to_bin(n)
    new_bin = ''
    for x in range(32-len(bin)):
        new_bin += '1'
    for i in range(len(bin)):
        if bin[i] == '0':
            new_bin += '1'
        else:
            new_bin += '0'
    return bin_to_dec(new_bin)


if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        n = int(input())
        result = flippingBits(n)
        print(result)
