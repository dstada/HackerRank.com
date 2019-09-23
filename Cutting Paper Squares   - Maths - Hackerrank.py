def solve(n, m):
    return (n-1) + (n * (m-1))

if __name__ == '__main__':

    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])

    result = solve(n, m)
    print(result)


# https://www.hackerrank.com/challenges/p1-paper-cutting/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign