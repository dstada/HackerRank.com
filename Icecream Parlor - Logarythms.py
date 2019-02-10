def icecreamParlor(m, arr):
    sort_arr = sorted(arr)
    tot = m - 1
    i, j = 0, 0
    while tot != m:     # Zolang totaal van 2 elementen niet gelijk is aan het budget
        tot = sort_arr[0+i] + sort_arr[len(arr)-1-j]
        if tot < m:
            print("{} lager dan budget {}".format(tot, m))
            i += 1
        elif tot > m:
            print("Tot te hoog")
            j += 1
        else:
            if arr.index(sort_arr[0+i]) < arr.index(sort_arr[len(arr)-1-j]):
                return str(arr.index(sort_arr[0+i])+1) + str(arr.index(sort_arr[len(arr)-1-j])+1)
            else:
                return  str(arr.index(sort_arr[len(arr) - 1 - j])+1) + str(arr.index(sort_arr[0 + i])+1)


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