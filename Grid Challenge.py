import math
import os
import random
import re
import sys


def gridChallenge(grid):        # grid is like: ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
    sorted_grid = []
    no = False
    for row in grid:            # Voor elke regel (= ingevoerd woord)
        sorted_grid.append(sort_string(row))    # Zet woord op alf. volgorde en voeg toe aan sorted_grid
    for i in range(len(grid[0])):  # Doe dit zo vaak als er en woord letters heeft:
        strg = ""
        for j in range(len(grid)):  # zo vaak doen als het aantal woorden
            strg += sorted_grid[j][i]
        if strg != sort_string(strg):
            no = True
            break
    if no is True:
        print("NO")
    else:
        print("YES")


def sort_string(a):
    return ''.join(sorted(a))




if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)


"""
1       # 1 setje
5       # aantal woorden
ebacd
fghij
olmkn
trpqs
xywuv

Output:
YES

3
3
abc
lmp
qrt
3
mpxz
abcd
wlmf
4
abc
hjk
mpq
rtv

Output: 
YES
NO
YES

https://www.hackerrank.com/challenges/grid-challenge/problem?h_r=next-challenge&h_v=zen
"""