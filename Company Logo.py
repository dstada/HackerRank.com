import math
import os
import random
import re
import sys
from operator import itemgetter


if __name__ == '__main__':
    s = list(input())
    print(s)
    s_set = set(s)
    print(s_set)
    d = [[c, s.count(c)] for c in s_set]
    print(d)
    e = sorted(d)
    print(e)
    f = e.sort(key=itemgetter(1), reverse=True)
    print(f)

"""
Input:
aabbbccde

Output:
b 3
a 2
c 2
"""