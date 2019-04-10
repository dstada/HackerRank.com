# https://www.hackerrank.com/challenges/lisa-workbook/problem


def workbook(n, k, arr):
    specials = 0
    bladzijde = 1
    for a in arr:       # for each chapter
        for i in range(1, a+1):     # for each problem in the chapter
            if i == bladzijde:      # problem number same as page number
                specials += 1
            if i % k == 0:          # reached the max nbr of problems on the page
                bladzijde += 1
        if a % k != 0:              # All problems on the pages. If place left: new page.
            bladzijde += 1
    return specials


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    arr = list(map(int, input().rstrip().split()))
    result = workbook(n, k, arr)
    print(result)


"""
input:

5 3
4 2 6 1 10

output:

4

"""