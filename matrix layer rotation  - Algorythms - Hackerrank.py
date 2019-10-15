

def matrixRotation(matrix, r):
    print(matrix)
    print("Aantal schillen: {}".format(int(min(len(matrix), len(matrix[0]))/2)))



if __name__ == '__main__':
    mnr = input().rstrip().split()
    m = int(mnr[0])
    n = int(mnr[1])
    r = int(mnr[2])
    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)



"""https://www.hackerrank.com/challenges/matrix-rotation-algo/problem
Input:

4 4 2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

Output:

3 4 8 12
2 11 10 16
1 7 6 15
5 9 13 14
"""