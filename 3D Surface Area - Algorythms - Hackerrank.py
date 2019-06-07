"""
https://3dwarehouse.sketchup.com/search/?q=3d%20surface%20area%20problem%20hackerrank%20com

https://www.hackerrank.com/challenges/3d-surface-area/problem

input:
6 1
1
1
1
1
1
1


input:
1 1
1

output: 6

input:
3 3
1 3 4
2 2 3
1 2 4

output: 60

input:
3 4
1 3 4 2
2 2 3 1
1 2 4 1

output: 70

input:
1 6
0 1 2 3 2 1

Output: 34
"""

def surfaceArea(A):
    surfaces = 0
    # len(A) is aantal regels, dus eerste ingevoerde waarde
    if len(A[0]) == 1:
        print("len(A) == 1")


    for i in range(len(A)): # For every rule:
        # Voor- en achtervlakken
        if len(A) == 1:
            surfaces += 2 * sum(A[i])
            print("voor/achter dubbel want slechts 1 rij: {}".format(surfaces))
        else:
            if i == 0 or i == len(A)-1:     # De vlakken van eerste en laatste regel
                surfaces += sum(A[i])
            print("voor/achter erbij: {}".format(surfaces))

        for j in range(len(A[i])):  # For every column:
            if len(A[0]) == 1:      # lengte van de rij slechts 1
                surfaces += 2 * A[i][j]     # Komt maar een keer langs, dus 2x tellen.
            else:
                if j == 0 or j == len(A[i])-1: # Left and right:
                    surfaces += A[i][j]
                    print("l en r: {}".format(surfaces))
            if A[i][j] > 0:
                surfaces += 2   # Bottom and top:
                print("{} - onder/boven erbij: {}".format(A[i][j],surfaces))
            if j > 0:
                # Absolute difference with previous column:
                surfaces += abs(A[i][j] - A[i][j-1])
                print("l/r tussenin: {}".format(surfaces))
    # Areas between front and back:
    for l in range(len(A[0])):
        for m in range(len(A)):
            if m > 0:
                surfaces += abs(A[m][l] - A[m-1][l])
    return surfaces


if __name__ == '__main__':
    HW = input().split()
    H = int(HW[0])
    W = int(HW[1])
    A = []
    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))
    result = surfaceArea(A)
    print(result)
