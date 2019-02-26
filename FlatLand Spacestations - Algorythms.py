import math
import os
import random
import re
import sys


def flatlandSpaceStations(n, c):
    # zet c op volgorde:
    c = sorted(c)




    # # Naar boven afronden:
    # x = 22.2
    # print(math.ceil(x))
    # # --> 23


if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    c = list(map(int, input().rstrip().split()))
    result = flatlandSpaceStations(n, c)
    print(result)

"""
Input:
6 6
0 1 2 4 3 5

Output:
0

Input:
5 2
0 4

Output:
2

https://www.hackerrank.com/challenges/flatland-space-stations/problem

"""