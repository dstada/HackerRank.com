
import math


def counterGame(n):     # Louise starts first
    teller = 0
    while n > 1:        # Zolang 1 nog niet is bereikt het volgende
        teller += 1
        if ((n & (n-1)) == 0) and n > 0:    # als factor2
            print("{} is factor2. Nu delen door 2.".format(n))
            n /= 2
        else:                   # Geen factor van 2
            print("{} geen factor2.".format(n))
            for i in range(n - 1, 2, -1):       # Zoek eerstvolgende factor 2 getal, terugtellend.
                if ((i & (i - 1)) == 0) and i > 0:  # Factor 2 getal gevonden
                    n -= i                          # Van n nu de kleinere factor2 aftrekken
    # Als het goed is, is n nu 1
    if n == 1:
        print("teller: {}".format(teller))
    print(n)



if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        result = counterGame(n)
        print(result)


"""https://www.hackerrank.com/challenges/counter-game/problem






input:
1
6

output:
Richard
"""
