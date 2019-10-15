

def matrixRotation(matrix, r):
    print(matrix)
    schil1 = []
    regels = len(matrix)
    kolommen = len(matrix[0])
    print("Aantal schillen: {}".format(int(min(regels, kolommen)/2)))
    # Maak list van buitenste schil:
    # Eerste regel toevoegen:
    for l in range(kolommen):
        schil1.append(matrix[0][l])
    # laatste elementen van tussenregels toevoegen:
    for i in range(1, regels - 1):
        laatste = matrix[i][-1]
        schil1.append(laatste)
    # laatste regel omgekeerd toevoegen:
    # for m in range(regels)
    schil1.append(matrix[regels-1][::-1])
    # eerste elementen van tussenregels toevoegen:
    for j in range(regels - 2, 0, -1):
        eerste = matrix[j][:1]
        schil1.append(eerste)
    print(schil1)


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