
import numpy

n, m = map(int, input().split())
# (n = rows and n = columns)

my_array = numpy.array([input().split() for _ in range(n)], int)
print(my_array)
print(my_array.transpose())
print(my_array.flatten())


"""
Input:
2 2
1 2
3 4
Output
[[1 3]
 [2 4]]
[1 2 3 4]

https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem?h_r=next-challenge&h_v=zen
"""