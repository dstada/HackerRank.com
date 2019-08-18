
def findPoint(px, py, qx, qy):
    print(qx + (qx - px), qy + (qy - py))


if __name__ == '__main__':
    n = int(input())

    for n_itr in range(n):
        pxPyQxQy = input().split()

        px = int(pxPyQxQy[0])

        py = int(pxPyQxQy[1])

        qx = int(pxPyQxQy[2])

        qy = int(pxPyQxQy[3])

        findPoint(px, py, qx, qy)


