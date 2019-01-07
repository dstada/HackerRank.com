
n = int(input())
lst = list(map(int, input().split()))
print(all(item > 0 for item in lst) and any(item == int((str(item))[::-1]) for item in lst))

"""
Task:
You are given a space separated list of integers. If all the integers are positive,
then you need to check if any integer is a palindromic integer.
For example:  88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202
Input:
5
12 9 61 5 14

Output: True
"""