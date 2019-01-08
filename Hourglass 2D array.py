def hourglassSum(arr):
    maximum = -100000
    for i in range(len(arr[0]) - 2):
        for j in range(len(arr[0]) - 2):
            tot = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            # print(arr[i][j], arr[i][j+1], arr[i][j+2], arr[i+1][j+1], arr[i+1][j+2], arr[i+2][j], arr[i+2][j+1], arr[i+2][j+2])
            # print(tot)
            if tot > maximum:
                maximum = tot
    return maximum


if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    result = hourglassSum(arr)
    print(result)

"""
https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
output: 19

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 9 2 -4 -4 0
0 0 0 -2 0 0
0 0 -1 -2 -4 0
output: 13
"""