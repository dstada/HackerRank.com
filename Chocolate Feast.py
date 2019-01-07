def chocolateFeast(n, c, m):    # n is budget, c is prijs p/stuk, m is aantal wrappers voor nieuwe bar
    buy = wraps = n // c
    while (wraps >= m):      # zolang er genoeg wrappers zijn om een bar te kopen
        buy += 1                # een bar erbij gekocht
        wraps -= m - 1       # van aantal wrappers gaat eraf: aantal wrappers voor een buy - 1
    return buy




if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        ncm = input().split()
        n = int(ncm[0])
        c = int(ncm[1])
        m = int(ncm[2])
        result = chocolateFeast(n, c, m)
        print(result)

"""
3
10 2 5
12 4 4
6 2 2
Output:
6
3
5
"""