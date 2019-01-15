

def maximumToys(prices, k):
    prices = sorted(prices)
    if prices[0] > k:
        return 0
    else:
        sum = 0
        counter = 0
        for price in prices:
            sum += price
            if sum <= k:
                counter += 1
            else:
                break
        return counter


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    prices = list(map(int, input().rstrip().split()))
    result = maximumToys(prices, k)
    print(result)


"""
https://www.hackerrank.com/challenges/mark-and-toys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

7 50
1 12 5 111 200 1000 10

Output:
4
(= An integer that denotes the maximum number of toys Mark can buy for his son.)

Not working for all caes:

def maximumToys(prices, k):
    if k < min(prices):
        print(k, sum(prices), min(prices))
        return 0
    else:
        prices2 = [i for i in prices if i <= k]   # Maak array van alle prices die niet groter dan budget zijn
        import itertools
        out_list = []
        # Maak list van alle mogelijke combinaties
        for i in range(1, len(prices2) + 1):
            out_list.extend(itertools.combinations(prices2, i))
        print(out_list)
        # Maak list van alle combinaties die samen niet groter dan budget zijn:
        totals = []
        for comb in out_list:
            if sum(comb) <= k:
                totals.append(len(comb))
        print(totals)
        print(max(totals))
"""