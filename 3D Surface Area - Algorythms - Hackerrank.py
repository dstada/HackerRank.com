"""
Input:
3 3
1 3 4
2 2 3
1 2 4

Output
60
"""

def surfaceArea(A):
    print(A)
    surfaces = 0
    for i in range(len(A)): # Voor elke regel invoer:
        if i == 0 or i == len(A)-1:
            print("voor/achterkant: {}".format(sum(A[i])))
            surfaces += sum(A[i])
        for j in range(len(A[i])):  # Voor elke kolom in de regel:
            print(A[i][j])
            if j == 0 or j == len(A[i])-1: # De vlakken aan rechter- en linkerkant
                surfaces += A[i][j]
            surfaces += 2   # Voor boven- en onderkant
            if j > 0:   # alleen 2e t/m rest
                # Absolute verschil met vorige:
                surfaces = surfaces + abs(A[i][j] - A[i][j-1])
        print(surfaces)
    # Areas between front and back:
    # for k in range(len(A)):
    print("------------------------")

    for l in range(len(A[0])):
        print("l: {}".format(l))
        for m in range(len(A)):
            print("m: {}".format(m))




if __name__ == '__main__':
    HW = input().split()
    H = int(HW[0])
    W = int(HW[1])
    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))
    result = surfaceArea(A)
    print(result)