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
    print("hoi")

if __name__ == '__main__':
    HW = input().split()
    H = int(HW[0])
    W = int(HW[1])
    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))
    result = surfaceArea(A)
    print(result)