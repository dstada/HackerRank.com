def happyLadybugs(b):
    print(b)



if __name__ == '__main__':
    g = int(input())
    for g_itr in range(g):
        n = int(input())
        b = input()
        result = happyLadybugs(b)


"""
Input:
5
5
AABBC
7
AABBC_C
1
_
10
DD__FQ_QQF
6
AABCBC

Output:
NO
YES
YES
YES
NO

https://www.hackerrank.com/challenges/happy-ladybugs/problem
"""