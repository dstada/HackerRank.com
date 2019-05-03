"""
Create an algorithm that checks any solved sudoku's validity.

Examples:
Input: [
    [3, 5, 2, 9, 1, 8, 6, 7, 4],
    [8, 9, 7, 2, 4, 6, 5, 1, 3],
    [6, 4, 1, 7, 5, 3, 2, 8, 9],
    [7, 8, 3, 5, 6, 9, 4, 2, 1],
    [9, 2, 6, 1, 3, 4, 7, 5, 8],
    [4, 1, 5, 8, 2, 7, 9, 3, 6],
    [8, 6, 4, 3, 7, 5, 8, 9, 2],
    [2, 7, 8, 4, 9, 1, 3, 6, 5],
    [5, 3, 9, 6, 8, 2, 1, 4, 7]
  ]
Output: false

Input: [
    [3, 5, 2, 9, 1, 8, 6, 7, 4],
    [8, 9, 7, 2, 4, 6, 5, 1, 3],
    [6, 4, 1, 7, 5, 3, 2, 8, 9],
    [7, 8, 3, 5, 6, 9, 4, 2, 1],
    [9, 2, 6, 1, 3, 4, 7, 5, 8],
    [4, 1, 5, 8, 2, 7, 9, 3, 6],
    [1, 6, 4, 3, 7, 5, 8, 9, 2],
    [2, 7, 8, 4, 9, 1, 3, 6, 5],
    [5, 3, 9, 6, 8, 2, 1, 4, 7]
  ]
Output: true
"""
# solution =  [
#     [3, 5, 2, 9, 1, 8, 6, 7, 4],
#     [8, 9, 7, 2, 4, 6, 5, 1, 3],
#     [6, 4, 1, 7, 5, 3, 2, 8, 9],
#     [7, 8, 3, 5, 6, 9, 4, 2, 1],
#     [9, 2, 6, 1, 3, 4, 7, 5, 8],
#     [4, 1, 5, 8, 2, 7, 9, 3, 6],
#     [1, 6, 4, 3, 7, 5, 8, 9, 2],
#     [2, 7, 8, 4, 9, 1, 3, 6, 5],
#     [5, 3, 9, 6, 8, 2, 1, 4, 7]
#   ]

solution = [
    [3, 5, 2, 9, 1, 8, 6, 7, 4],
    [8, 9, 7, 2, 4, 6, 5, 1, 3],
    [6, 4, 1, 7, 5, 3, 2, 8, 9],
    [7, 8, 3, 5, 6, 9, 4, 2, 1],
    [9, 2, 6, 1, 3, 4, 7, 5, 8],
    [4, 1, 5, 8, 2, 7, 9, 3, 6],
    [8, 6, 4, 3, 7, 5, 8, 9, 2],
    [2, 7, 8, 4, 9, 1, 3, 6, 5],
    [5, 3, 9, 6, 8, 2, 1, 4, 7]
  ]
sudoku = True
#  Horizontal check:
out = True      # In order to get out of two loops
for i in range(9):
    print(solution[i])
    # Maak set en tel. Moeten 9 unieke waarden zijn.
    if len(set(solution[i])) != 9:
        sudoku = False
        out = False
    if not out:
        break

# Vertical check:
for j in range(9):
    temp_vert = []
    for k in range(9):
        if solution[k][j] in temp_vert:
            sudoku = False
            break
        temp_vert.append(solution[k][j])

# Block check:
for l in range(0, 7, 3):
    for k in range(0, 7, 3):
        print("l: {} k: {} dus waarde: {}".format(l, k, solution[l][k]))
        temp_block = []
        for m in range(3):
            for n in range(3):
                print(m, n)

        # temp_block.append(solution[][])
        # print(solution[]][])


print(sudoku)