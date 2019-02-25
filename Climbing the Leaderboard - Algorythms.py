import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    print(scores)
    teller = 1
    for i in range(len(scores)):




if __name__ == '__main__':
    scores_count = int(input())
    scores = list(map(int, input().rstrip().split()))
    alice_count = int(input())
    alice = list(map(int, input().rstrip().split()))
    result = climbingLeaderboard(scores, alice)


"""
Input:
6
100 90 90 80 75 60
5
50 65 77 90 102

Output:
6
5
4
2
1

Input:
7
100 100 50 40 40 20 10
4
5 25 50 120

Output:
6
4
2
1

https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem?h_r=next-challenge&h_v=zen


"""