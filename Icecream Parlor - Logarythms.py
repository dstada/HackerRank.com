def icecreamParlor(m, arr):
    print(m, arr)
    print(sorted(arr))
    tot = m - 1
    i, j = 0, 0
    while tot != m:     # Zolang totaal van 2 elementen niet gelijk is aan het budget
        if arr[0+i] + arr[len(arr)-1-j] < m:
            i += 1
        elif arr[0+i] + arr[len(arr)-1-j] > m:
            j += 1
        else:
            print(i, j)
            # res_arr = str(arr[0+i]) + " " + str(arr[len(arr)-1-i])
            res_arr = str(arr.index(arr[0+i])) + " " + str(arr.index(arr[len(arr)-1-i]))
            # return res_arr






    # arr.index(value)

    return "check"


if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        m = int(input())
        n = int(input())
        arr = list(map(int, input().rstrip().split()))
        result = icecreamParlor(m, arr)
        print(result)

"""
https://www.hackerrank.com/challenges/icecream-parlor/problem
Input:
2
4
5
1 4 5 3 2
4
4
2 2 4 3

Output:
1 4
1 2
"""