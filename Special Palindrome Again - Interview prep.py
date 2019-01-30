# def check_special_palindrome(a):
#     nmbr = 0
#     for i in range(1, len(a)+1):
#         strg = a[0:i]
#         if len(set(strg)) > 2:
#             break
#         if len(strg) % 2 != 0 and len(strg) > 2:    # is odd
#             if strg[:len(strg) // 2] == strg[(len(strg) // 2) + 1:]:
#                 nmbr += 1
#         else:
#             if len(set(strg)) == 1:
#                 nmbr += 1
#     return nmbr
#
#
# def substrCount(n, s):
#     tot = 0
#     for i in range(len(s)):
#         tot += check_special_palindrome(s[i:])
#     print(tot)


def substrCount(n, s):
    count = n           # aantal letters in string
    for x in range(n):  # doe dit zo vaak als string lang is
        y = x               # y wordt de waarde van x
        while y < n - 1:    # zolang y  minder dan aantal letters in string - 1
            y += 1          # waarde y ophogen met 1
            if s[x] == s[y]:    # als letter van huidige letter gelijk is aan volgende letter
                print("s[x] == s[y] - {} {}".format(s[x], s[y]))
                count += 1      # teller ophogen met een
            else:
                if s[x:y] == s[y+1:2*y-x+1]:  # twee opvolgende letters niet gelijk aan elkaar, dan
                    print(s[x:y], s[y+1:2*y-x+1])   # letter twee posities vergelijken
                    count += 1
                break
    return count


if __name__ == '__main__':
    n = int(input())
    s = input()
    result = substrCount(n, s)
    print(result)


"""
5
asasd
Output: 7

Input:
7
abcbaba
Output: 10

4
aaaa
Output: 10

https://www.hackerrank.com/challenges/special-palindrome-again/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings


def check_special_palindrome(a):
    nmbr = 0
    for i in range(1, len(a)+1):
        strg = a[0:i]
        if len(strg) % 2 != 0 and len(strg) > 2:    # is odd
            strg = strg[:len(strg) // 2] + strg[(len(strg) // 2) + 1:]
        if len(set(strg)) == 1:
            nmbr += 1
    return nmbr


def substrCount(n, s):
    tot = 0
    for i in range(len(s)):
        tot += check_special_palindrome(s[i:])
    print(tot)
"""