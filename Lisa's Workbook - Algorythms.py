# https://www.hackerrank.com/challenges/lisa-workbook/problem

def workbook(n, k, arr):
    # n = aantal hoofdstukken
    # k = max. aantal problems per bladzijde
    # arr = aantal problems per hoofdstuk
    specials = 0
    bladzijde = 0
    for i in range(len(arr)):       # elk hoofdstuk afwerken:
        bladzijde += 1
        print("sowieso nieuwe blz. Nu: {}".format(bladzijde))
        for j in range(arr[i]):     # elk probleem langs:
            print("problem: {}".format(j + 1))
            # if j + 1 > k:           # als probleemteller > aantal problemen p/blz:
            #     print("Volgende blz.")
            #     bladzijde += 1      # bladzijde-teller ophogen
            # print("Blz: {}".format(bladzijde))
    # print(bladzijde)






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