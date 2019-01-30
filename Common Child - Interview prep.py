import difflib


def commonChild(s1, s2):
    s1a, s2a = "", ""
    for letter in s1:
        if letter in s2:
            s1a += letter
    for letter in s2:
        if letter in s1:
            s2a += letter
    print(s1a, s2a)
    matcher = difflib.SequenceMatcher(
        None, s1a, s2a)
    match = matcher.find_longest_match(
        0, len(s1a), 0, len(s2a))
    return match.size


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
"""