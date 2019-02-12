def closestNumbers(arr):
    arr_sorted = sorted(arr)
    for i in arr_sorted:
        print(i)



    return 10


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = closestNumbers(arr)
    print(result)

"""
Input:
10
-20 -3916237 -357920 -3620601 7374819 -7330761 30 6246457 -6461594 266854 
Sample Output:
-20 30

Input:
12
-20 -3916237 -357920 -3620601 7374819 -7330761 30 6246457 -6461594 266854 -520 -470 
Output:
-520 -470 -20 30

Input:
4
5 4 3 2
Output:
2 3 3 4 4 

https://www.hackerrank.com/challenges/closest-numbers/problem
"""