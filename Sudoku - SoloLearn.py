"""
Create an algorithm that checks any solved sudoku's validity.
Sudoku Validator
A solved sudoku puzzle is a matrix of typically 9*9 in which every row,
every column and every block contains every number from 1 to 9 exactly once.

Dick STADA - May 2019
"""

# solution = [            # output: True
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

solution = [            # output: False (vertically not OK (6th column))
    [3, 5, 2, 9, 1, 8, 6, 7, 4],
    [8, 9, 7, 2, 4, 6, 5, 1, 3],
    [6, 4, 1, 7, 5, 3, 2, 8, 9],
    [7, 8, 3, 5, 6, 9, 4, 2, 1],
    [9, 2, 6, 1, 3, 4, 7, 5, 8],
    [4, 1, 5, 8, 2, 7, 9, 3, 6],
    [1, 6, 4, 3, 7, 5, 8, 9, 2],
    [2, 7, 8, 4, 9, 1, 3, 6, 5],
    [2, 7, 8, 4, 9, 1, 3, 6, 5],
  ]

# solution = [            # output: False  (Horizontal not OK (7th line))
#     [3, 5, 2, 9, 1, 8, 6, 7, 4],
#     [8, 9, 7, 2, 4, 6, 5, 1, 3],
#     [6, 4, 1, 7, 5, 3, 2, 8, 9],
#     [7, 8, 3, 5, 6, 9, 4, 2, 1],
#     [9, 2, 6, 1, 3, 4, 7, 5, 8],
#     [4, 1, 5, 8, 2, 7, 9, 3, 6],
#     [8, 6, 4, 3, 7, 5, 8, 9, 2],
#     [2, 7, 8, 4, 9, 1, 3, 6, 5],
#     [5, 3, 9, 6, 8, 2, 1, 4, 7]
#   ]


def check_sudoku(solution):
    sudoku = True
    #  Horizontal check:
    for i in range(9):  # Check every line until not sudoku
        # check number of unique values in the row
        if len(set(solution[i])) != 9:
            sudoku = False

    # Vertical check:
    for j in range(9):
        temp_vert = []
        for k in range(9):
            # As soon as double value exists
            if solution[k][j] in temp_vert:
                sudoku = False
            temp_vert.append(solution[k][j])

    # Block check:
    for l in range(0, 7, 3):    # Each top left cel of a 3 x 3 block
        for k in range(0, 7, 3):
            temp_block = []
            for m in range(3):
                for n in range(3):
                    temp_block.append(solution[m+l][n+k])
            # check number of unique values in the 3 x 3 block
            if len(set(temp_block)) != 9:
                sudoku = False
    if sudoku is False:
        return "False"
    else:
        return "True"

print(check_sudoku(solution))
# TODO: print wrong cells









