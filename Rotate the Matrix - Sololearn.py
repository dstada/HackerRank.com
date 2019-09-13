""""Rotate the Matrix

Write a program that takes a NxN square matrix as an input
and rotates it clockwise by 90 degrees.

For example:
Input:
1  2  3
4  5  6
7  8  9
Output:
7  4  1
8  5  2
9  6  3
"""
def print_matrix(inpt, max):     # Prints the matrix nicely
    for k in range(n):
        s = ""
        for l in range(n):
            s += " " + " " * (max - len(str(inpt[k][l]))) + str(inpt[k][l])
        print(s)

# Build the original matrix:
n = int(input("Matrix height/width: "))
# Generate unrotated list:
lst = [[(i + j) for i in range(n)] for j in range(1, n * n, n)]

# Find out longest number:
max_len = 0
for x in range(n):
    for y in range(n):
        if len(str(lst[x][y])) > max_len:
            max_len = len(str(lst[x][y]))
print_matrix(lst, max_len)
# Rotate 90 degrees clockwise:
new_matrix = []
for j in range(n):
    temp = []
    for i in reversed(range(n)):
        temp.append(lst[i][j])
    new_matrix.append(temp)
print(20 * "-")
print_matrix(new_matrix, max_len)
