

from operator import xor


def maximizingXor(l, r):
    print(xor(bool(l), bool(r)))


if __name__ == '__main__':
    l = int(input())
    r = int(input())
    result = maximizingXor(l, r)
    print(result)

"""
11
100

Output: 127

https://www.hackerrank.com/challenges/maximizing-xor/problem?h_r=next-challenge&h_v=zen
"""