
import math


def counterGame(n):     # Louise starts first
    while n > 1:
        if ((n & (n-1)) == 0) and n > 0:    
            print("factor 2")
        else:                   # Geen factor van 2
            for i in range(n - 1, 2, -1):       # Zoek eerstvolgende factor 2 getal
                print(i)
                if ((i & (i - 1)) == 0) and i > 0:  # Factor 2 getal gevonden
                    n -= i
                    break
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
