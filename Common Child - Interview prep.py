
def commonChild(s1, s2):
    m, n = len(s1), len(s2)
    prev, cur = [0]*(n+1), [0]*(n+1)
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                cur[j] = 1 + prev[j-1]
            else:
                if cur[j-1] > prev[j]:
                    cur[j] = cur[j-1]
                else:
                    cur[j] = prev[j]
        cur, prev = prev, cur
    return prev[n]


# Te traag:
# def commonChild(s1, s2):
#     matrix = [["" for x in range(len(s2))] for x in range(len(s1))]
#     for i in range(len(s1)):
#         for j in range(len(s2)):
#             if s1[i] == s2[j]:
#                 if i == 0 or j == 0:
#                     matrix[i][j] = s1[i]
#                 else:
#                     matrix[i][j] = matrix[i-1][j-1] + s1[i]
#             else:
#                 matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1], key=len)
#
#     cs = matrix[-1][-1]
#
#     # return len(cs), cs
#     return len(cs)



if __name__ == '__main__':
    s1 = input()
    s2 = input()
    result = commonChild(s1, s2)
    print(result)


"""
https://www.hackerrank.com/challenges/common-child/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings&h_r=next-challenge&h_v=zen

Input:
WEWOUCUIDGCGTRMEZEPXZFEJWISRSBBSYXAYDFEJJDLEBVHHKS
FDAGCXGKCTKWNECHMRXZWMLRYUCOCZHJRRJBOAJOQJZZVUYXIC

Output: 15

Input:
HARRY
SALLY

Output: 2

Input:
AA
BB
Output: 0

Input:
SHINCHAN
NOHARAAA

Output: 3

Input:
ABCDEF
FBDAMN

Output:
2

With this you'll find the longest string which is in both strings.
So, without deleting any of the letters that both strings have in common:

    matcher = difflib.SequenceMatcher(
        None, s1a, s2a)
    match = matcher.find_longest_match(
        0, len(s1a), 0, len(s2a))
    return match.size

"""