def weightedUniformStrings(s, queries):
    scores = []
    for i in range(len(s)):
        scores.append(ord(s[i]) - 96)
        teller = 1
        while i + teller != len(s) and s[i] == s[i+teller]:
            print("Nog eentje")
            teller += 1
        else:
            print("Niet nog meer dezelfde.")
            teller = 1
            break

    print(scores)


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

def weightedUniformStrings(s, queries):
    scores = set()
    ctr = 1
    for i in range(len(s)):
        score = ord(s[i]) - 96
        if i + 1 != len(s) and s[i + 1] == s[i]:
            ctr = ctr + 1
        else:
            1
        scores.add(score * ctr)
    print(scores)
"""