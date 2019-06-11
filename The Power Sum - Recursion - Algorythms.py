"""
Python program to count number of ways
to express x as sum of n-th power
of unique natural numbers.

https://www.hackerrank.com/challenges/the-power-sum/problem

Inputs:

10
2

100
2

100
3

Outputs:

1

3

1
"""

def countWaysUtil(x, n, num):
    # Base cases
    val = (x - pow(num, n))
    if (val == 0):
        return 1
    if (val < 0):
        return 0

    # Consider two possibilities, num is
    # included and num is not included.
    return countWaysUtil(val, n, num + 1) + \
           countWaysUtil(x, n, num + 1)


def powerSum(X, N):
    return countWaysUtil(X, N, 1)


if __name__ == '__main__':
    X = int(input())
    N = int(input())
    result = powerSum(X, N)
    print(result)