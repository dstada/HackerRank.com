import numpy

my_array = list((map(int, input("").split())))
my_array = numpy.array(my_array)
print(numpy.reshape(my_array, (3, 3)))

"""
#Output
[[1 2]
[3 4]
[5 6]]

1 2 3 4 5 6 7 8 9
Sample Output

[[1 2 3]
 [4 5 6]
 [7 8 9]]

https://www.hackerrank.com/challenges/np-shape-reshape/problem
"""