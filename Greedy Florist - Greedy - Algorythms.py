

def getMinimumCost(k, c):
    c = sorted(c, reverse=True)
    costs = 0
    teller = 0
    for i in range(0, len(c)):
        costs += (i // k + 1) * c[i]
        # print("Costs nu: {}".format(costs))
    return costs


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    c = list(map(int, input().rstrip().split()))
    minimumCost = getMinimumCost(k, c)
    print(minimumCost)


"""https://www.hackerrank.com/challenges/greedy-florist/problem?h_r=next-challenge&h_v=zen

input:
3 3
2 5 6

output: 13
------------------------
input:
3 2
2 5 6

output: 15
------------------------
input:
5 3
1 3 5 7 9

output:
29
------------------------
"""