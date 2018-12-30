import operator

if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])      # aantal atleten
    m = int(nm[1])      # aantal attributen
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))    # attribuutwaarden per regel in list zetten
    # arr wordt dan bijv. [[10, 2, 5], [7, 1, 0], [9, 9, 9], [1, 23, 12], [6, 5, 9]]

    for i in sorted(arr, key=operator.itemgetter(int(input()))):
        print(*i)


"""
5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1

Output:
7 1 0
10 2 5
6 5 9
9 9 9
1 23 12
"""