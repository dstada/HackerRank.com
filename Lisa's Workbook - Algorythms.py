# https://www.hackerrank.com/challenges/lisa-workbook/problem


def workbook(n, k, arr):
    specials = 0
    bladzijde = 1
    for i in range(len(arr)):       # elk hoofdstuk afwerken:
        print("---- blz: {}".format(bladzijde))
        for j in range(arr[i]):     # elk probleem langs:
            print("j+1: {} - k: {}".format(j+1, k))
            if (j + 1) % k == 0:           # als probleemteller > aantal problemen p/blz:
                bladzijde += 1      # bladzijde-teller ophogen
                print("Volgende blz. Nu: {}".format(bladzijde))
            print("blz: {} - problem: {}".format(bladzijde, j+1))
            if bladzijde == j + 1:
                specials += 1
                print(">>>> specials: {}".format(specials))
        bladzijde += 1
    print(bladzijde)


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