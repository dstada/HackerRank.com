def bomberMan(n, grid):
    print(n, grid, len(grid))
    print("-------------")
    gridnew = len(grid) * [len(grid) * "0"]
    print(gridnew)

    # Van 0 naar 3:

    if n % 2 == 0:
        gridnew = n * [n * "0"]
        return gridnew          # Every even s the grid is filled

    if n == 1:      # After 1 s is the situation the same as in s=0
        return grid
    """
    if (n%4==3) return set2;
    return set3;
    """

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
"""