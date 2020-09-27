__author__ = 'Dick Stada'
import sys
import math


def restaurant(l, b):
    if l == b:
        return 1
    if l >= b:
        hoogste = l
        laagste = b
    else:
        hoogste = b
        laagste = l
    ggd = math.gcd(hoogste, laagste)
    blokjes = (laagste / ggd) * (hoogste / ggd)
    return int(blokjes)


if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        lb = input().split()
        l = int(lb[0])
        b = int(lb[1])
        result = restaurant(l, b)
        print(str(result) + '\n')

