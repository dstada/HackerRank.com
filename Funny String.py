import math
import os
import random
import re
import sys


def funnyString(s):
    left = [ord(cijfer) for cijfer in s]
    diff_left = [abs(left[i+1] - left[i]) for i in range(len(left)-1)]
    right = left[::-1]
    diff_right = [abs(right[i+1] - right[i]) for i in range(len(right)-1)]
    if diff_left == diff_right:
        print("Funny")
    else:
        print("Not Funny")


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        # fptr.write(result + '\n')

    # fptr.close()

"""
Input:
2
acxz
bcxz

Output:
Funny
Not Funny

https://www.hackerrank.com/challenges/funny-string/problem?h_r=next-challenge&h_v=zen
"""