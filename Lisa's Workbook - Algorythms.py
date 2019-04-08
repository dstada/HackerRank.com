# https://www.hackerrank.com/challenges/lisa-workbook/problem

def workbook(n, k, arr):
    # n = aantal hoofdstukken
    # k = max. aantal problems per bladzijde
    # arr = aantal problems per hoofdstuk
    specials = 0
    bladzijde = 1
    for i in range(len(arr)):       # elk hoofdstuk afwerken:
        for j in range(1, arr[i] + 1):     # elk probleem langs:
            print("problem: {}".format(j))
            if j + 1 > k:           # als probleemteller > aantal problemen p/blz:
                print("Volgende blz.")
                bladzijde += 1      # bladzijde-teller ophogen
            print("Blz: {}".format(bladzijde))
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