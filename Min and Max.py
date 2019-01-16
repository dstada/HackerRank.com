
# Leg n en m vast vanuit de eerste input-regel:
import numpy

n, m = map(int, input().split())

# Vul de numpy-array met elke regel input:
a = numpy.array([input().split() for _ in range(n)], int)
print(a)

print(numpy.max(numpy.min(a, axis=1), axis=0))
"""

You are given a 2-D array with dimensions N X M.
Your task is to perform the min function over axis 1 and then find the max of that.

Input Format

The first line of input contains the space separated values of N and N.
The next N lines contains M space separated integers.

Output Format

Compute the min along axis 1 and then print the max of that result.

Sample Input
4 2
2 5
3 7
1 3
4 0
Sample Output
3
"""