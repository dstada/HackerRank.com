

def cavityMap(grid):
    print(grid)
    arr = [grid[0]]
    print(arr)
    for i in range(1, len(grid) - 1):
        print(grid[i])
        for j in range(1, len(grid[i]) - 1):
            u = int(grid[i - 1][j])
            l = int(grid[i][j - 1])
            r = int(grid[i][j + 1])
            d = int(grid[i + 1][j])
            if u < int(grid[i][j]) and l < int(grid[i][j]) and r < int(grid[i][j]) and d < int(grid[i][j]):
                print("X")
    arr.append(grid[--1])
    print(arr)


if __name__ == '__main__':
    n = int(input())
    grid = []
    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)
    result = cavityMap(grid)
    print(result)

"""https://www.hackerrank.com/challenges/cavity-map/problem?h_r=next-challenge&h_v=zen

Input:
4
1112
1912
1892
1234

Output:
1112
1X12
18X2
1234
"""