def happyLadybugs(b):
    print(b)
    # At least one char is the only of that kind:
    for letter in b:
        if letter != '_' and b.count(letter) < 2:
            print("NO")
            break
    # Check if existing ladybugs are happy now:
    for i in range(len(b)):
        print(i)


    return 10


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