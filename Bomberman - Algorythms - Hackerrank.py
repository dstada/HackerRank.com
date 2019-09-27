def bomberMan(n, grid):
    print(grid)

    if n % 2 == 0:     # Every even s the grid is filled
        grid2 = len(grid) * [len(grid[0]) * "O"]
        return grid2

    if n == 1:          # After 1 s is the situation the same as in s=0
        return grid     # Return the same grid as the input grid

    if n % 4 == 3:      # s = 3, 7, 11, 15, etc. After detonation of the bombs.
        grid3 = []
        for i in range(len(grid)):
            print("Rij {}".format(i))
            print(grid[i])
            rule = ""
            for j in range(len(grid[0])):
                if grid[i][j] == "O":
                    rule += "."
                elif j > 0:
                    if grid[i][j - 1] == "O":   # Left of it is a bomb
                        rule += "."
                # elif grid[i][j + 1] == 'O' and j + 1 <= len(grid[0]):  # Right of it is a bomb
                        rule += "."
                # # elif grid[i - 1][j] == 'O':  # Above of it is a bomb
                # #         rule += "."
                # # elif grid[i + 1][j] == 'O':  # Below is a bomb
                # #         rule += "."
                else:
                    rule += "O"
            print(rule)
        # return grid3

    # return set3     # s = 5, 9, 13, 17, enz


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