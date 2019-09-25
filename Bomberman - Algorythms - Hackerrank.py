def bomberMan(n, grid):
    print(n, grid, len(grid))
    print("-------------")

    if n % 2 == 0:     # Every even s the grid is filled
        gridnew = len(grid) * [len(grid[0]) * "O"]
        return gridnew

    if n == 1:      # After 1 s is the situation the same as in s=0
        return grid

    if n % 4 == 3:
        return set2

    return set3


if __name__ == '__main__':
    rcn = input().split()
    r = int(rcn[0])
    c = int(rcn[1])
    n = int(rcn[2])
    grid = []
    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)
    result = bomberMan(n, grid)
    print(result)

"""Sample:
Input:

6 7 3
.......
...O...
....O..
.......
OO.....
OO.....

Output:

OOO.OOO
OO...OO
OOO...O
..OO.OO
...OOOO
...OOOO

Input:
6 7 5
.......
...O.O.
....O..
..O....
OO...OO
OO.O...

Output:
.......
...O.O.
...OO..
..OOOO.
OOOOOOO
OOOOOOO

6 7 1
.......
...O.O.
....O..
..O....
OO...OO
OO.O...

Output:
.......
...O.O.
...OO..
..OOOO.
OOOOOOO
OOOOOOO

https://www.hackerrank.com/challenges/bomber-man/problem
"""