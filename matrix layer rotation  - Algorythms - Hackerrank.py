
def matrixRotation(matrix, r):
    print(matrix)
    regels = len(matrix)
    kolommen = len(matrix[0])
    print("Aantal schillen: {}".format(int(min(regels, kolommen)/2)))
    # Buitenste schil:
    # Eerste regel toevoegen:
    schil1 = []
    for l in range(kolommen):
        schil1.append(matrix[0][l])
    # laatste elementen van tussenregels toevoegen:
    for i in range(1, regels - 1):
        laatste = matrix[i][-1]
        schil1.append(laatste)
    # laatste regel omgekeerd toevoegen:
    for q in matrix[regels-1][::-1]:
        schil1.append(q)
    # eerste elementen van tussenregels toevoegen:
    for j in range(regels - 2, 0, -1):
        eerste = matrix[j][0]
        schil1.append(eerste)
    # roteren van de schil met een plek:
    schil1.append(schil1.pop(0))
    print(schil1)

    # Binnenste (tweede) schil:
    schil2 = []
    # Eerste regel toevoegen:
    for a in range(1, kolommen - 1):
        schil2.append(matrix[1][a])
    # Rechterkolom toevoegen:
    for p in range(2, regels - 2):
        laatst = matrix[p][kolommen - 2]
        schil2.append(laatst)
    # Onderste regel omgekeerd toevoegen:
    for b in range(kolommen - 2, 0, -1):
        schil2.append(matrix[regels - 2][b])
    # eerste elementen van tussenregels toevoegen:
    for v in range(regels - 3, 1, -1):
        eerst = matrix[v][1]
        schil2.append(eerst)
    # roteren van de schil met een plek:
    schil2.append(schil2.pop(0))
    print(schil2)

    # Omzetten van de nieuwe schillen naar een nieuwe matrix:
    schil1_def = []
    # Eerste regel:
    schil1_def.append(schil1[0:kolommen])
    print(schil1_def)
    # Tussenregels:
    # 1e en laatste uit schil1, tussenin 1e regel van schil2
    # Laatste regel
    #


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
Input:
5 4 7
1 2 3 4
7 8 9 10
13 14 15 16
19 20 21 22
25 26 27 28
Output:
28 27 26 25
22 9 15 19
16 8 21 13
10 14 20 7
4 3 2 1

5 5 1
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25

"""