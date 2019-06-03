"""
https://3dwarehouse.sketchup.com/search/?q=3d%20surface%20area%20problem%20hackerrank%20com

https://www.hackerrank.com/challenges/3d-surface-area/problem

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

"""

def surfaceArea(A):
    surfaces = 0
    if A == [[1]]:
        return 6

    for i in range(len(A)): # For every rule:
        if i == 0 or i == len(A)-1:
            surfaces += sum(A[i])
        print("voor/achter erbij: {}".format(surfaces))
        for j in range(len(A[i])):  # For every column:
            if j == 0 or j == len(A[i])-1: # Left and right:
                surfaces += A[i][j]
                print("l en r: {}".format(surfaces))
            surfaces += 2   # Bottom and top:
            print("onder/boven erbij: {}".format(surfaces))
            if j > 0:
                # Absolute difference with previous column:
                surfaces += abs(A[i][j] - A[i][j-1])
                print("l/r tussenin: {}".format(surfaces))
    print(surfaces)
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
