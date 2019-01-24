
import numpy


n, m, p = map(int, input().split())
arr1 = numpy.array([input().split() for _ in range(n)], int)
print(arr1)
arr2 = numpy.array([input().split() for _ in range(m)], int)
print(arr2)

print(numpy.concatenate((arr1, arr2), axis = 0))
"""
Input

4 3 2
1 2
1 2
1 2
1 2
3 4
3 4
3 4

Output

[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]]

https://www.hackerrank.com/challenges/np-concatenate/problem?h_r=next-challenge&h_v=zen
"""