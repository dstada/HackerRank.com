def gameWithCells(n, m):
    hor = n // 2 + (n - (2 * (n // 2)))
    ver = m // 2 + (m - (2 * (m // 2)))
    return hor * ver


if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    print(gameWithCells(n, m))
