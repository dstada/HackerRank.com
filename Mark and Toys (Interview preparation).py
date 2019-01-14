

def maximumToys(prices, k):
    print(prices)
    print(k)
    prices2 = [i for i in prices if i <= k]
    print(prices2)
    import itertools
    out_list = []
    for i in range(1, len(prices2) + 1):
        out_list.extend(itertools.combinations(prices2, i))
    print(out_list)


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    prices = list(map(int, input().rstrip().split()))
    result = maximumToys(prices, k)

"""
https://www.hackerrank.com/challenges/mark-and-toys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

7 50
1 12 5 111 200 1000 10

Output:
4
"""