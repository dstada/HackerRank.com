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
            print("{} hoger dan budget {}".format(tot, m))
            j += 1
        else:
            print("tot {} gelijk aan budget {}".format(tot, m))
            if sort_arr[0 + i] == sort_arr[len(arr) - 1 - j]:
                search_value = sort_arr[0 + i]
                print("Beide cijfers zijn gelijk")
                # Nu 2 verschillende indexen vinden:
                first = arr.index(search_value)
                print("first {}".format(first))
                print("Tweede index komt uit rest van arr:")
                print("Rest is: arr[first+1: {}".format(arr[first+1:]))
                second = arr[first+1:].index(search_value) + 1
                print("second {}".format(second))
                return str(first+1) + str(second+1)
            elif arr.index(sort_arr[0+i]) < arr.index(sort_arr[len(arr)-1-j]):    # Laagste waarde voorop
                return str(arr.index(sort_arr[0+i])+1) + str(arr.index(sort_arr[len(arr)-1-j])+1)
            else:
                return str(arr.index(sort_arr[len(arr) - 1 - j])+1) + str(arr.index(sort_arr[0 + i])+1)


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

Input:
3
9
6
1 3 4 6 7 9
8
6
1 3 4 4 6 8
3
2
1 2
Your Output (stdout)
2 4
3 2
1 2
Expected OutputDownload
2 4
3 4
1 2
"""