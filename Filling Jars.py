def solve(n, operations):
    # n = nr of jars
    # m = nr of rounds
    # operations s bijv. [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
    jars = [[] for i in range(n)]
    for j in range(len(operations)):
        print(j)
        for x in range(operations[j][0], operations[j][1]+1):

        jars[operations[j] = operations[j][2]
    print(jars)


if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    operations = []
    for _ in range(m):
        operations.append(list(map(int, input().rstrip().split())))
    result = solve(n, operations)


"""
https://www.hackerrank.com/challenges/filling-jars/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

Input:

5 3
1 2 100
2 5 100
3 4 100

Output: 160
"""