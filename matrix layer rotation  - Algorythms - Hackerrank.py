import math


def matrixRotation(matrix, r):
    # print(matrix)
    regels = len(matrix)
    kolommen = len(matrix[0])
    schillen_n = math.ceil((min(regels, kolommen) / 2))
    schillen = []
    for i in range(schillen_n):  # Dit voor elke schil doen:
        schil = []
        schil_top = []  # Bovenkant
        for a in range(i, kolommen - i):
            schil_top.append(matrix[i][a])

        schil_rechts = []  # Rechts
        schil_links = []  # links
        if (regels - 2 - i * 2) > 0:  # alleen als er een rechts kan zijn:
            for j in range(1 + i, regels - 1 - i):
                schil_rechts.append(matrix[j][kolommen - 1 - i])
            for k in range(regels - 1 - i, 1 + i, -1):
                schil_links.append(matrix[k - 1][0 + i])

        schil_bottom = []  # Onderkant
        for q in range(kolommen - i, i, -1):
            schil_bottom.append(matrix[regels - i - 1][q - 1])

        schil.extend(schil_top)
        schil.extend(schil_rechts)
        schil.extend(schil_bottom)
        schil.extend(schil_links)
        schillen.append(schil)
    print("schillen: {}".format(schillen))

    # Roteren:
    schillen_rotated = []
    for schil in schillen:
        schil.append(schil.pop(0))
        schillen_rotated.append(schil)
    print(schillen_rotated)

    print("######################################")
    #
    # # NIEUWE MATRIX MAKEN:
    # # Omzetten van de nieuwe schillen naar een nieuwe matrix (bij 2 schillen):
    # schil1_def = []
    # # Eerste regel:
    # schil1_def.append(schil1[0:kolommen])
    # print(schil1_def)
    # # Tussenregels:
    # print("Aantal tussenregels: {}".format(regels - 2))
    # # 1e en laatste uit schil1, tussenin 1e regel van schil2
    # # Eerst de buitenste getallen links en rechts per regel:
    # tussenrls = int((len(schil2) - 2 * (kolommen - 2)) / 2)
    # for x in range(1, regels - 1):
    #     if x == 1:
    #         print(x, "Eerste regel uit schil2")
    #         print(schil2[0:kolommen - 2])
    #     elif x == regels - 2:
    #         print(x, "Laatste regel uit schil2")
    #         print(schil2[kolommen - 2 + tussenrls: kolommen - 2 + tussenrls + kolommen - 2][::-1])
    #     else:
    #         print(x, "Tussenregel uit schil2")
    #         # Eerste en laatste van tussenregel schil2:
    #         print(schil2[len(schil2) - x + 1], schil2[kolommen - 2])
    #
    #     # Aan elkaar:
    #     schil1_def.append([schil1[len(schil1) - x], schil1[kolommen - 1 + x]])
    #
    # # Laatste regel
    # print(schil1[kolommen + (regels - 2):kolommen + (regels - 2) + kolommen])
    # schil1_def.append(schil1[kolommen + (regels - 2):kolommen + (regels - 2) + kolommen][::-1])
    # print(schil1_def)


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

4 4 1
 1  2  3  4
 5  6  7  8
 9 10 11 12
13 14 15 16

 2  3  4  8
 1  7 11 12
 5  6 10 16
 9 13 14 15

6 6 1
1 2 3 4 5 6
7 8 9 10 11 12
13 14 15 16 17 18
19 20 21 22 23 24
25 26 27 28 29 30
31 32 33 34 35 36


kan niet:
5 5 1
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15 
16 17 18 19 20
21 22 23 24 25

output:
2 3 4 5 10
1 8 9 13 15
6 7 13 19 20
11 12 17 18 25
16 21 22 23 24

"""