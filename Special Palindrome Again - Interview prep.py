
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


if __name__ == '__main__':
    n = int(input())
    s = input()
    result = substrCount(n, s)
    # print(result)


"""
5
asasd
Output: 7

Input:
7
abcbaba
Output: 10

https://www.hackerrank.com/challenges/special-palindrome-again/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
"""