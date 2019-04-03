
import math


def counterGame(n):     # Louise starts first
    arr = [1, 2]
    while arr[-1] < n:
        arr.append(arr[-1]*2)
    print(arr)
    teller = 0
    while n > 1:        # Zolang 1 nog niet is bereikt het volgende
        teller += 1
        if n in arr:    # als factor2
            n /= 2
        else:                   # Geen factor van 2
    #         for i in range(n - 1, 2, -1):       # Zoek eerstvolgende factor 2 getal, terugtellend.
    #             if (i & (i - 1)) == 0:  # Factor 2 getal gevonden
    #                 n -= i                          # Van n nu de kleinere factor2 aftrekken
    # if teller % 2 == 0:
    #     return "Richard"
    # else:
    #     return "Louise"




if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        result = counterGame(n)
        print(result)


"""https://www.hackerrank.com/challenges/counter-game/problem


def counterGame(n):     # Louise starts first
    teller = 0
    while n > 1:        # Zolang 1 nog niet is bereikt het volgende
        teller += 1
        if (n & (n-1)) == 0:    # als factor2
            n /= 2
        else:                   # Geen factor van 2
            for i in range(n - 1, 2, -1):       # Zoek eerstvolgende factor 2 getal, terugtellend.
                if (i & (i - 1)) == 0:  # Factor 2 getal gevonden
                    n -= i                          # Van n nu de kleinere factor2 aftrekken
    if teller % 2 == 0:
        return "Richard"
    else:
        return "Louise"



input:
1
6

output:
Richard
"""
