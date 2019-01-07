from collections import namedtuple

n, ind = int(input()),(input().split()).index('MARKS')

print(sum([float((input().split())[ind]) for i in range(n)])/n, end = "0")

"""
5
ID         MARKS      NAME       CLASS
1          97         Raymond    7
2          50         Steven     4
3          91         Adrian     9
4          72         Stewart    5
5          80         Peter      6

Output:
78.00
"""