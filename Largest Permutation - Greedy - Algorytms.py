
def largestPermutation(k, arr):
    print(arr)
    # print(arr.index(max(arr)))
    arr_new = []
    for i in range(len(arr) - 1):       # Van links naar rechts in getal
        print("arr[i] {} - arr[i+1:] {} - max(arr(i+1:]) {}".format(arr[i], arr[i+1:], max(arr[i+1:])))
        if arr[i] < max(arr[i+1:]):     # Kijk of er grotere waardes in de rest zitten
            indx = arr.index(max(arr[i+1:]))    # Zoek de index van de grootste waarde
            # zet hogere op de plaats van arr[i]
            for x in arr[:i]: arr_new.append(x)
            arr_new.append(arr[indx])

            print(arr_new)



    return ""

if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    arr = list(map(int, input().rstrip().split()))
    result = largestPermutation(k, arr)
    print(result)



"""
input:
5 1
4 2 3 5 1

output:
5 2 3 4 1
--------------
input:
5 2
4 3 2 5 1

output:
5 4 2 3 1

https://www.hackerrank.com/challenges/largest-permutation/problem?h_r=next-challenge&h_v=zen

input:
3 1
2 1 3

output:
3 1 2
------------------

input:
2 1
2 1

output:
2 1


"""