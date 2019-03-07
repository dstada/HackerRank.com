#!/bin/python3


def lonelyinteger(a):
    setje = list(set(a))
    if len(setje) == 1:  # All numbers are the same
        return list(set(a))[0]
    for nmbr in setje: # Tel voor elk voorkomend cijfer of het een oneven aantal voorkomt in a
        if a.count(nmbr) % 2 != 0:
            return nmbr


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    result = lonelyinteger(a)
    print(result)

"""https://www.hackerrank.com/challenges/lonely-integer/problem

Inputs:
3
1 1 2

1
1

5
0 0 1 2 1

Outputs:
2

1

2

"""