def detonation(grid):
    grid3 = []
    for i in range(len(grid)):
        # print("Rij {}".format(i))
        # print(grid[i])
        rule = ""
        for j in range(len(grid[0])):
            if grid[i][j] == "O":  # Here is a bomb
                rule += "."
            elif j > 0 and grid[i][j - 1] == "O":  # Left of it is a bomb
                rule += "."
            elif j < len(grid[0]) - 1 and grid[i][j + 1] == "O":  # Right is a bomb
                rule += "."
            elif i > 0 and grid[i - 1][j] == "O":  # Above is a bomb
                rule += "."
            elif i < len(grid) - 1 and grid[i + 1][j] == "O":  # Beneath it is a bomb
                rule += "."
            else:
                rule += "O"
        print(rule)
        grid3.append(rule)
    return grid3


def bomberMan(n, grid):
    print(grid)

    if n % 2 == 0:     # Every even s the grid is filled
        grid2 = len(grid) * [len(grid[0]) * "O"]
        return grid2

    if n == 1:          # After 1 s is the situation the same as in s=0
        return grid     # Return the same grid as the input grid

    if n % 4 == 3:      # s = 3, 7, 11, 15, etc. After detonation of the bombs.
        grid4 = detonation(detonation(grid))
        return grid4

    print("Kennelijk is n nu 5, 9, 13, enz")
    grid4 = detonation(grid)     # s = 5, 9, 13, 17, enz. So, the situation after detonation in grid3.
    grid5 = detonation(grid4)
    return grid5


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