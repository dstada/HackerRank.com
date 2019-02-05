def check_happy(b):
    overall_happy = True
    for i in range(len(b)):
        print(i)
        happy = False
        # If left or right is the same colour bug, then happy:
        if (i - 1 >= 0 and b[i - 1] == b[i]) or i + 1 < len(b) and b[i + 1] == b[i]:
            happy = True
        else:
            print("Niet happy")
            overall_happy = False
        print(happy)
    return overall_happy


def happyLadybugs(b):
    # At least one char is the only of that kind:
    for letter in b:
        if letter != '_' and b.count(letter) < 2:
            return "NO"
            # break
    # Check if existing ladybugs are happy now:
    if check_happy(b) is True:
        return "YES"
    else:
        #TODO: Kijk hoe de ladybugs toch blij kunnen worden
        print("Kijken of ze blij kunnen worden")


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