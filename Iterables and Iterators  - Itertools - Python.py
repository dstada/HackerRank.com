from itertools import combinations

n = int(input())        # number of letters
s = input().split()     # splitted string of letters
k = int(input())        # number of indices
# print(n, s, k)

nbr = s.count("a")      # number of a's in string
l = list(combinations(s, k))    # list of all combinations
# print(l)
total = 0
for i in range(len(l)):
    if "a" in l[i][0] or "a" in l[i][1]:
        total += 1
print(total / len(l))


"""
https://www.hackerrank.com/challenges/iterables-and-iterators/problem

Input:
4
a a c d
2

Output:
0.8333

"""