
from collections import defaultdict

d = defaultdict(list)
# n is aantal elementen in A
# m is aantal elementen in B
n, m = list(map(int, input().split()))
# elk element aan A toevoegen. n-keer dus:
for i in range(n):
    d[input()].append(i + 1)        # Voeg aan d toe: input-letter als index en aantal als (ophogende) waarde
print(d)
# nu voor elk element in B:
for i in range(m):                  # Voor elke input voor B:
    print(' '.join(map(str, d[input()])) or -1)     # de waarde die hoort bij index als input + spatie

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

https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
"""