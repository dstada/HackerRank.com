from random import randint

a, b = 97, 122
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
print(grid_dict)
# print(grid[2][3])       # Eerst regel, dan x-e letter van die regel
for i in range(0, hor):
    for j in range(0,ver):
        print(grid[i][j])
        if i-1 >= 0:        # boven
            print("boven: {}".format(grid[i-1][j]))
            if grid[i][j] == grid[i-1][j]:
                grid_dict[grid[i][j]] += 1
        if i+1 < len(grid):  # onder
            print("onder: {}".format(grid[i+1][j]))
        if i-1 >= 0 and j-1 >= 0:   # linksboven
            print("linksboven: {}".format(grid[i-1][j-1]))
        if i-1 >= 0 and j+1 < len(grid):
            print("rechtsboven: {}".format(grid[i-1][j+1]))
        if i + 1 < len(grid) and j + 1 < len(grid):
            print("rechtsonder: {}".format(grid[i + 1][j + 1]))
        if i+1 < len(grid) and j-1 >= 0:
            print("linksonder: {}".format(grid[i+1][j-1]))
        if j-1 >= 0:        # links
            print("links: {}".format(grid[i][j-1]))
        if j+1 < len(grid):  # rechts
            print("rechts: {}".format(grid[i][j+1]))

        print("--------------")

print(grid_dict)



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