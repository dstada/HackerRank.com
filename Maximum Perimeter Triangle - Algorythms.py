n = int(input())
sticks = sorted(int(i) for i in input().split())
# sticks is op volgorde van laag naar hoog

i = n-3
# Beginnen bij de laatste drie en dan naar links toe werken zolang geen driehoek mogelijk is:
while i >= 0 and (sticks[i] + sticks[i+1] <= sticks[i+2]):
    i -= 1

if i >= 0:
    print(sticks[i], sticks[i+1], sticks[i+2])
else:
    print(-1)

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
# Onderstaande werkt niet voor alle cases:
# import itertools
#
# def maximumPerimeterTriangle(sticks):
#     combs = list(itertools.combinations(sticks, 3))
#     max_peri = -1
#     max_comb = 0
#     for comb in combs:
#         if comb[0] + comb[1] > comb[2]:
#             if comb[0]+comb[1]+comb[2] > max_peri:
#                 max_peri = comb[0]+comb[1]+comb[2]
#                 max_comb = combs.index(comb)
#     if max_peri == -1:
#         return -1
#     else:
#         return combs[max_comb]


# if __name__ == '__main__':
#     n = int(input())
#     sticks = list(map(int, input().rstrip().split()))
#     result = maximumPerimeterTriangle(sticks)
#     print(result)
#
