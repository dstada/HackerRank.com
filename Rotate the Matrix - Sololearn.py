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
# Build the original matrix:
n = int(input("Matrix height/width: "))

lst = [[(i + j) for i in range(n)] for j in range(1, n * n, n)]

for y in range(n):
    print(lst[y])

print(lst)

# Rotate clockwise 90 degrees:
new_matrix = []
for j in range(n):
    temp = []
    for i in reversed(range(n)):
    # print(i) # van hoogste naar laagste
        print(i, j)
        temp.append(lst[i][j])
    print(temp)
    new_matrix.append(temp)

print(new_matrix)