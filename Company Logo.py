import math
import os
import random
import re
import sys
from operator import itemgetter


if __name__ == '__main__':
    s = list(input())
    s_set = set(s)
    d = [[c, s.count(c)] for c in s_set]
    e = sorted(d)
    e.sort(key=itemgetter(1), reverse=True)
    teller = 0
    for pair in e:
        if teller < 3:
            print("{} {}".format(pair[0], pair[1]))
            teller += 1

"""
Input:
aabbbccde

Output:
b 3
a 2
c 2
"""