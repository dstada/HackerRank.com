import math
import os
import random
import re
import sys


# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    print(scores)
    teller = 1
    # sorteer alice an laag naar hoog
    print(sorted(alice))



    # for i in range(len(alice)):
    #     print("{} op plek {}".format(alice[i], i))
    #     # bekijk elk element van scores en voeg tussen
    #     for j in range(len(scores)):
    #         # Pak element, kijk of score alie groter gelijk of kleiner is
    #         if alice[i] > scores[j]:        # score alice groter dan element in scores:
    #             # alice invoegen vóór scores
    #             print("{} groter dan {}".format(alice[i], scores[j]))
    #             scores =  [alice[i]] + scores
    #             print(scores)
    #             break
    #         elif alice[i] == scores[j]:
    #             print("{} gelijk aan {}".format(alice[i], scores[j]))
    #             break
    #         else:
    #             print("{} kleiner dan {}".format(alice[i], scores[j]))






    # for i in range(1, len(scores)):     # Vanaf het 2e item
    #     if scores[i] < scores[i-1]:
    #         teller += 1
    #     print(scores[i], teller)



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