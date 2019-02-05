def check_happy(b):
    overall_happy = True
    for i in range(len(b)):
        happy = False
        # If left or right is the same colour bug, then happy:
        if (i - 1 >= 0 and b[i - 1] == b[i]) or i + 1 < len(b) and b[i + 1] == b[i]:
            happy = True
        else:
            overall_happy = False
    return overall_happy


def happyLadybugs(b):
    # At least one char is the only of that kind:
    for letter in b:
        if letter != '_' and b.count(letter) < 2:
            return "NO"
    # Check if existing ladybugs are happy now:
    if check_happy(b) is True:
        return "YES"
    else:
        if b.count("_") == 0:
            for i in range(1, n - 1):
                if b[i - 1] != b[i] and b[i + 1] != b[i]:   # No similar neighbours
                    return "NO"
        return "YES"                # Empty place(s)

if __name__ == '__main__':
    g = int(input())
    for g_itr in range(g):
        n = int(input())
        b = input()
        result = happyLadybugs(b)
        print(result)

"""
Input:
5
5
AABBC
7
AABBC_C
1
_
10
DD__FQ_QQF
6
AABCBC

Output:
NO
YES
YES
YES
NO

https://www.hackerrank.com/challenges/happy-ladybugs/problem
"""