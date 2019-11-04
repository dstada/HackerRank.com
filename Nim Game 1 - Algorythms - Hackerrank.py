def nimGame(a):
    s = a[0]
    for i in range(1, len(a)):
        s ^= a[i]
    if s == 0:
        return "Second"
    else:
        return "First"


if __name__ == '__main__':
    g = int(input())
    for g_itr in range(g):
        n = int(input())
        pile = list(map(int, input().rstrip().split()))
        result = nimGame(pile)
        print(result)

"""
https://www.hackerrank.com/challenges/nim-game-1/problem
input:

2
2
1 1
3
2 1 4

output:

Second
First


"""