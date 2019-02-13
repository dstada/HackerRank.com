

def findMedian(arr):
    arr_sort = sorted(arr)
    print(arr_sort)
    print(arr_sort[len(arr) // 2])


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = findMedian(arr)
    print(result)

"""
Input:
7
Output:
0 1 2 4 6 5 3

https://www.hackerrank.com/challenges/find-the-median/problem?h_r=next-challenge&h_v=zen
"""