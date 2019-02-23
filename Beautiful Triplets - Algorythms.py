def beautifulTriplets(d, arr):
    triple = 0
    for i in range(len(arr)):
        if arr[i] + d in arr and arr[i] + 2*d in arr:
            triple += 1
    return triple


if __name__ == '__main__':
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    arr = list(map(int, input().rstrip().split()))
    result = beautifulTriplets(d, arr)
    print(result)

"""https://www.hackerrank.com/challenges/beautiful-triplets/problem?h_r=next-challenge&h_v=zen

Input:
7 3
1 2 4 5 7 8 10

Output:
3

Input:
5 1
2 2 3 4 5

Output:
3

"""