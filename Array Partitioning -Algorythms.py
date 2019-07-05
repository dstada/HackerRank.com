"""
Array Partitioning

Divide a given array of numbers into two subarrays such that the absolute difference
between their sums is the smallest possible. For example, the array [2, 5, 4, 7, 15, 20]
can be divided into subarrays [15, 7, 4] and [20, 5, 2]. The difference between the sums
of those arrays is 1, and it is the smallest.

For example:
Input:
6
4, 15, 20, 2, 7, 5

Output:
[15, 7, 4]
[20, 5, 2]
1
(The sum of the first subarray is 26, the sum of the second subarray is 27, the difference is 1.)
"""
import itertools
# Opvragen array:

arr = list(map(int, input("Give some numbers, separated by a space: ").rstrip().split()))
# Make absolute numbers:
arr2 = []
for nmbr in arr:
    print(nmbr)
    arr2.append(abs(nmbr))
print(arr2)

# itertools.combinations(iterable, r)
# r is lengte van de combinatie
# lijst = list(itertools.combinations(iterable, r))
lijst = list(itertools.combinations(arr, 3))
print(lijst)

