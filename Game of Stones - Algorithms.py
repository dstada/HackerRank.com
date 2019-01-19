
def gameOfStones(n):
    print(n)
    if n % 7 < 2:   # Modulo --> 0 or 1
        return "Second"
    else:
        return "First"


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = gameOfStones(n)
        print(result)

"""
8
1
2
3
4
5
6
7
10

Output:
Second
First
First
First
First
First
Second
First
"""