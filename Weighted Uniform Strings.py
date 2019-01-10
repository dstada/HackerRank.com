def weightedUniformStrings(s, queries):
    teller = 1
    vorige = ''
    gewichten = []
    for c in s:     # Voor elke letter uit s:
        if c != vorige:
            teller = 1
            vorige = c
            gewichten.append(ord(c) - 96)
        else:
            teller += 1
            gewichten.append(teller * (ord(c) - 96))

    print(gewichten)
    for q in queries:
        if q in s:
            return "Yes"
        else:
            return "No"


if __name__ == '__main__':
    s = input()
    queries_count = int(input())
    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)
    print(result)

"""
https://www.hackerrank.com/challenges/weighted-uniform-string/problem?h_r=next-challenge&h_v=zen
Input:
abccddde
6
1
3
12
5
9
10
Output:
Yes
Yes
Yes
Yes
No
No
"""