

def toys(w):
    w.sort()
    i = 0
    basis = 0
    containers = 1
    while i < len(w):               # Zolang i kleiner dan lengte array
            if w[i] <= w[basis] + 4:        # Als huidige w[i] kleiner of gelijk aan 'uitgangs-w[]':
                    i += 1                  # i ophogen
            else:                       # verschil groter dan 4
                    basis = i                 # uitgangs-w' verschuiven naar i
                    containers += 1         # aantal containers ophogen
    return containers


if __name__ == '__main__':
    n = int(input())
    w = list(map(int, input().rstrip().split()))
    result = toys(w)
    print(result)


"""
https://www.hackerrank.com/challenges/priyanka-and-toys/problem

Input:
8
1 2 3 21 7 12 14 21

Output:
4

Input:
8
1 2 3 4 5 10 11 12

Output:
2


def toys(w):
    w = sorted(list(set(w)))
    print((w))
    i = 0
    min = i
    containers = 0
    while i < len(w):                 # Zolang i niet verder dan laatste element van w
        while w[i] - w[min] <= 4:     # Zolang laatste min eerste niet groter dan 4:
            i += 1                    # Teller ophogen om volgend element te bekijken
        else:
            containers += 1           # grootste min kleinste > 4, dus weer een container
            min = i                   # min wordt verzet naar nieuwe i
            i += 1
    print(containers)
"""