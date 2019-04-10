# https://www.hackerrank.com/challenges/tower-breakers-1/problem


def towerBreakers(n, m):
    if m == 1 or n % 2 == 0:
        return 2
    else:
        return 1


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nm = input().split()
        n = int(nm[0])
        m = int(nm[1])
        result = towerBreakers(n, m)
        print(result)