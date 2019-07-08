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

https://code.sololearn.com/c2aIBKvuMA46/#py
"""


def array_partition(arr):
    arr.sort(key=int, reverse=True)
    left = []
    right = []
    left.append(arr[0])
    for i in range(1,len(arr)):
        if sum(left) >= sum(right):
            right.append(arr[i])
        else:
            left.append(arr[i])
    print(left)
    print(right)
    print(abs(sum(left)-sum(right)))


m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
array_partition(ar)
