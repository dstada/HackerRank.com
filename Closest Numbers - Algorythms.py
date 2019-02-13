def closestNumbers(arr):
    arr_sorted = sorted(arr)
    min_diff = 1000000000000000000000000
    min_diff_values = []
    for i in range(len(arr_sorted)-1):
        print(i)
        diff = abs(arr_sorted[i] - arr_sorted[i+1])
        if diff == min_diff:
            min_diff_values.extend((arr_sorted[i], arr_sorted[i + 1]))
        if diff < min_diff:
            min_diff = diff
            min_diff_values = []
            min_diff_values.extend((arr_sorted[i], arr_sorted[i + 1]))
    return min_diff_values


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = closestNumbers(arr)
    print(result)
"""
Input:
4
5 4 3 2
Output:
2 3 3 4 4 5

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

https://www.hackerrank.com/challenges/closest-numbers/problem
"""