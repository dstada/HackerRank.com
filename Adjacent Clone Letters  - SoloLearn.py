from random import randint

# Laagste en hoogste waarde ascii-tabel:
a, b = 97, 122

# Create dict
grid_dict = {}

# tussenijst maken:
new_list = []

# Vraag om de afmetingen van het grid:
lst = list(map(int, input("Give number of rows and columns, seperated by a space: ").split()))
hor = lst[0]
ver = lst[1]
# Maak grid aan:
grid = []
for i in range(0, hor):
    new = []
    for j in range(0, ver):
        new.append(chr(randint(a, b)))
    grid.append(new)
# print(grid[2][3])       # Eerst regel, dan x-e letter van die regel

# Set maken van de waarden in grid:
for i in range(len(grid)):
    for j in range(len(grid[0])):
        new_list.append(grid[i][j])
for letter in new_list:
    grid_dict[letter] = 0



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