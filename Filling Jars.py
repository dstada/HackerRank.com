

def solve(n, operations):
    # n = nr of jars
    # m = nr of rounds
    # operations s bijv. [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
    total = 0
    for item in operations:        # voor elk element van operations
        total += (item[1] - item[0] + 1) * item[2]
    return int(total / n)


if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    operations = []
    for _ in range(m):
        operations.append(list(map(int, input().rstrip().split())))
    result = solve(n, operations)
    print(result)


"""
https://www.hackerrank.com/challenges/filling-jars/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

Input:

5 3
1 2 100
2 5 100
3 4 100

Output: 160

Gives time-out:

def solve(n, operations):
    # n = nr of jars
    # m = nr of rounds
    # operations s bijv. [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
    jars = [0 for i in range(n)]
    for item in operations:        # voor elk element van operations
        van = item[0]
        tot = item[1]
        for i in range(van - 1, tot):
            jars[i] += item[2]
    return int(sum(jars) / n)

"""