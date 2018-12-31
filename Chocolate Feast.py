def chocolateFeast(n, c, m):
    buy = 0
    wrap = 0
    while n // c > 0:   # Zolang budget > prijs per stuk
        buy += n // c   # buy is budget gedeeld door prijs per stuk
        wrap += buy     # verpakkingen erbij vanwege aankopen


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

6
3
5
"""