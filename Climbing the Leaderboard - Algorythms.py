import math
import os
import random
import re
import sys


def climbingLeaderboard(scores, alice):
    scores_set = list(set(scores))
    # scores_set is niet geordend
    scores_set.sort(reverse=True)
    # nu is scores_set geordend van hoog naar laag
    result = []
    lengte = len(scores_set)
    for s in alice:     # Voor elk element in alice
        # zolang lente>0 en element in alice groter dan actuele score:
        while (lengte > 0) and (s >= scores_set[lengte - 1]):
            lengte -= 1                 # lengte verlagen met 1
        result.append(lengte + 1)
        # element van alice nu kleiner dan actuele score --> rang volgens Dense Ranking toevoegen aan de array result
    return result


if __name__ == '__main__':
    scores_count = int(input())
    scores = list(map(int, input().rstrip().split()))
    alice_count = int(input())
    alice = list(map(int, input().rstrip().split()))
    result = climbingLeaderboard(scores, alice)
    print(result)

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