from itertools import combinations

n = int(input())        # number of letters
s = input().split()     # splitted string of letters
k = int(input())        # number of indices
# print(n, s, k)

nbr = s.count("a")      # number of a's in string
l = list(combinations(s, k))    # list of all combinations
total = 0

if k > n - nbr:
    print(1.0)
else:
    for i in range(len(l)):
        if "a" in l[i]:     # count number of a's in all combinations
            total += 1
    print(total / len(l))   # percentage of elements with an a in it


"""
https://www.hackerrank.com/challenges/iterables-and-iterators/problem

Input:
4
a a c d
2

Output:
0.8333

INput:
9
a b c a d b z e o
4

Output:
0.722222222222

"""