import math
import os
import random
import re
import sys


def flatlandSpaceStations(n, c):
    # zet c op volgorde:
    c = sorted(c)
    # eerste verschil (tussen beginpunt en eerste station
    diff = [c[0] - 0]
    print(diff)
    for i in range(len(c) - 1):
        print("Voeg toe")
        diff.append(c[i+1] - c[i])
    print(c[-1])
    print(n-1)
    diff.append(c[-1] - (n-1))
    print(diff)


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