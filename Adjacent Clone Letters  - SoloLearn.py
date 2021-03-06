from random import randint

# a, b = 97, 122  kleine letters
a, b = 65, 90
grid_dict = {}
new_list = []
lst = list(map(int, input("Give number of rows and columns, seperated by a space: ").split()))
hor = lst[0]
ver = lst[1]
grid = []
for i in range(0, hor):
    new = []
    for j in range(0, ver):
        new_letter = chr(randint(a, b))
        new.append(new_letter)
        new_list.append(new_letter)
    grid.append(new)
for row in grid:
    print(row)
for letter in set(new_list):
    grid_dict[letter] = 0
for i in range(0, hor):
    for j in range(0, ver):
        if i-1 >= 0 and j-1 >= 0:
            if grid[i][j] == grid[i-1][j-1]:
                grid_dict[grid[i][j]] += 1
        if i - 1 >= 0:
            if grid[i][j] == grid[i - 1][j]:
                grid_dict[grid[i][j]] += 1
        if i-1 >= 0 and j+1 < ver:
            if grid[i][j] == grid[i-1][j+1]:
                grid_dict[grid[i][j]] += 1
        if j-1 >= 0:
            if grid[i][j] == grid[i][j-1]:
                grid_dict[grid[i][j]] += 1
        if j+1 < ver:
            if grid[i][j] == grid[i][j+1]:
                grid_dict[grid[i][j]] += 1
        if i+1 < hor and j-1 >= 0:
            if grid[i][j] == grid[i+1][j-1]:
                grid_dict[grid[i][j]] += 1
        if i+1 < hor:
            if grid[i][j] == grid[i+1][j]:
                grid_dict[grid[i][j]] += 1
        if i + 1 < hor and j + 1 < ver:
            if grid[i][j] == grid[i+1][j+1]:
                grid_dict[grid[i][j]] += 1

for letter in grid_dict:
    if grid_dict[letter] > 0:
        print("{} = {} adjacent clones".format(letter.upper(), grid_dict[letter]))


"""
https://www.sololearn.com/learn/4682/?ref=app

Suppose you have a 2D array of letters. A letter is adjacent to another if it is positioned either at the top, bottom,
left, right, upper left, upper right, lower left or lower right of the other.

Create a program that accepts the dimensions of a 2D array and fills that array with random letters.
Then search through the array for adjacent similar letters.
Indicate which letters have adjacent clones and enumerate them.

For example:
Input: 5x4
Output:
  Array:
    A C T T  S
    R T N G T
    E E G G A
    U W P F A
  Results:
    T = 4 adjacent clones
    G = 3 adjacent clones
    E = 2 adjacent clones
    A = 2 adjacent clones
"""