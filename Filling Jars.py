

def solve(n, operations):
    # n = nr of jars
    # m = nr of rounds
    # operations s bijv. [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
    # jars = [[] for i in range(n)]
    jars = [0 for i in range(n)]
    van = 0
    tot = 0
    for item in operations:        # voor elk element van operations
        van = item[0]
        tot = item[1]
        print("van {} tot {}".format(van, tot))
        for i in range(van - 1, tot):
            print(i)
            print(item[2])
            print(type(item[2]))
            print(jars[i])
            jars[i] += item[2]
    print(jars)
    print(sum(jars) / len(jars))


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