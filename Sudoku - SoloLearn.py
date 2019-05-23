"""
Create an algorithm that checks any solved sudoku's validity.

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

# solution = [            # output: False (vertically not OK (6th column))
#     [3, 5, 2, 9, 1, 8, 6, 7, 4],
#     [8, 9, 7, 2, 4, 6, 5, 1, 3],
#     [6, 4, 1, 7, 5, 3, 2, 8, 9],
#     [7, 8, 3, 5, 6, 9, 4, 2, 1],
#     [9, 2, 6, 1, 3, 4, 7, 5, 8],
#     [4, 1, 5, 8, 2, 7, 9, 3, 6],
#     [1, 6, 4, 3, 7, 5, 8, 9, 2],
#     [2, 7, 8, 4, 9, 1, 3, 6, 5],
#     [2, 7, 8, 4, 9, 1, 3, 6, 5],
#   ]

solution = [            # output: False  (Horizontal not OK (7th line))
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


def check_sudoku(solution):
    sudoku = True
    #  Horizontal check:
    for i in range(9):  # Check every line until not sudoku
        # print(solution[i])
        # Create set and count. Should be 9 unique values.
        # print(len(set(solution[i])))
        if len(set(solution[i])) != 9:
            sudoku = False
            return sudoku

    print("Horizontal oké!")

    # Vertical check:
    for j in range(9):
        temp_vert = []
        for k in range(9):
            # As soon as double value exists
            if solution[k][j] in temp_vert:
                sudoku = False
                print("vertically not OK...")
                print(temp_vert)    # vlak voordat dezelfde waarde wordt toegevoegd die al een keer voorkomt
                return sudoku
            temp_vert.append(solution[k][j])
    print("vertically OK!")


# Block check:
for l in range(0, 7, 3):    # Each top left cel
    print("l: {}".format(l))
    for k in range(0, 7, 3):
        print("k: {}".format(k))
        temp_block = []
        for m in range(3):
            for n in range(3):
                print(m, n)
        temp_block.append(solution[m][n])
        print(solution[m][n])

print(check_sudoku(solution))



# def check_sudoku(matrix):
#     sudoku = True
#     out = True      # In order to get out of two loops
#     for i in range(9):
#         print(solution[i])
#         #  Horizontal check:
#         # Create set and count. Should be 9 unique values.
#         print(len(set(solution[i])))
#         if len(set(solution[i])) != 9:
#             sudoku = False
#             out = False
#             print("horizontaal niet oke")
#             return sudoku
#         if out:             # Horizontally OK
#             print("Horizontal OK!")
#             # Vertical check:
#             print("Vertical check")
#             for j in range(9):
#                 temp_vert = []
#                 for k in range(9):
#                     # As soon as double value exists
#                     if solution[k][j] in temp_vert:
#                         sudoku = False
#                         return sudoku
#                     temp_vert.append(solution[k][j])
#             print(temp_vert)
#             # Vertically also OK, now block check:
#             for l in range(0, 7, 3):    # Each top left cel
#                 print(l)
#                 for k in range(0, 7, 3):
#                     temp_block = []
#                     for m in range(3):
#                         for n in range(3):
#                             print(m, n)
#
#                     temp_block.append(solution[m][n])
#                     print(solution[m][n])
#
print(check_sudoku(solution))







