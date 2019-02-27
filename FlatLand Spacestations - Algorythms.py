import math
import os
import random
import re
import sys


def flatlandSpaceStations(n, c):
    # n is aantal steden
    # c is index van de stations
    # zet c op volgorde:
    c = sorted(c)
    # eerste verschil (tussen beginpunt en eerste station
    diff = [abs(c[0] - 0)]
    # de verschillen tussen de stations in:
    for i in range(len(c) - 1):
        diff.append(int((c[i+1] - c[i])/2))
    # verschil tussen laatste station en laatste stad:
    diff.append(abs(c[-1] - (n-1)))
    return max(diff)


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