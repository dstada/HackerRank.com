
from collections import defaultdict

d = defaultdict(list)
# n is aantal elementen in A
# m is aantal elementen in B
n, m = list(map(int, input().split()))
# elk element aan A toevoegen. n-keer dus:
for i in range(n):
    d[input()].append(i + 1)
print(d)
# nu voor elk element in B:
for i in range(m):
    print(' '.join(map(str, d[input()])) or -1)

"""
Input:
5 2
a
a
b
a
b
a
b

defaultdict(<class 'list'>, {'a': [1, 2, 4], 'b': [3, 5]})

Output:
1 2 4
3 5
"""