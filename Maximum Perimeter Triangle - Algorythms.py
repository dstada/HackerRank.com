import itertools

def maximumPerimeterTriangle(sticks):
    combs = list(itertools.combinations(sticks, 3))
    max_peri = -1
    max_comb = 0
    for comb in combs:
        if comb[0] + comb[1] > comb[2]:
            if comb[0]+comb[1]+comb[2] > max_peri:
                max_peri = comb[0]+comb[1]+comb[2]
                max_comb = combs.index(comb)
    if max_peri == -1:
        return -1
    else:
        return combs[max_comb]

if __name__ == '__main__':
    n = int(input())
    sticks = list(map(int, input().rstrip().split()))
    result = maximumPerimeterTriangle(sticks)
    print(result)


"""
https://www.hackerrank.com/challenges/maximum-perimeter-triangle/problem?h_r=next-challenge&h_v=zen

Input:
6
1 1 1 2 3 5

Output:
1 1 1

Input:
50
1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000
Output
1000000000 1000000000 1000000000
"""