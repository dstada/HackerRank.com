
def largestPermutation(k, arr):
    # print(arr.index(max(arr)))
    for i in range(len(arr) - 1):
        print(arr[i])

    return ""

if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    arr = list(map(int, input().rstrip().split()))
    result = largestPermutation(k, arr)
    print(result)



"""
https://www.hackerrank.com/challenges/largest-permutation/problem?h_r=next-challenge&h_v=zen

input:
3 1
2 1 3

output:
3 1 2

input:
2 1
2 1

output:
2 1

input:
5 1
4 2 3 5 1

output:
5 2 3 4 1
"""