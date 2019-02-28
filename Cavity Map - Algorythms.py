

def cavityMap(grid):
    arr = [grid[0]]     # Eerste regel naar nieuwe grid, want geen X mogelijk.
    print(arr)
    for i in range(1, len(grid) - 1):       # Tussenregels checken op cavity
        print("We bekijken: {}".format(grid[i]))
        new_line = grid[i]                # eerst de bestaande regel overnemen
        # print("new_line: {}".format(new_line))
        for j in range(1, len(grid[i]) - 1):
            u = int(grid[i - 1][j])
            l = int(grid[i][j - 1])
            r = int(grid[i][j + 1])
            d = int(grid[i + 1][j])
            if u < int(grid[i][j]) and l < int(grid[i][j]) and r < int(grid[i][j]) and d < int(grid[i][j]):
                print("X")
                new_line = new_line[:j] + 'X' + new_line[j+1:]
        print(new_line)
        arr.append(new_line)
    arr.append(grid[-1])
    return arr


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

Input:
989
191
111

Output:
989
1X1
111

This one is better:

def cavityMap(grid):  
    s = ''.join(line for line in grid); t = s[:]
    l = len(grid[0]); n = len(grid)

    for i in range(l+1, (n-1)*l,l):
        for j in range(i, i+l-2):
            values = map(int, [s[j+1], s[j-1], s[j-l], s[j+l]])
            if int(s[j]) > max(values):
                t = ''.join([t[:j],'X',t[j+1:]])

    for i in range(0, n*l,l):
        yield t[i:i+l]
"""