# https://www.hackerrank.com/challenges/zig-zag-sequence/problem


def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2 - 1)        # index of center value
    print(a[mid], a[n-1])
    print("mid: {}".format(mid))
    a[mid], a[n-1] = a[n-1], a[mid]     # swap center value with highest value
    print(a[mid], a[n-1])
    st = mid + 1                    # index van eentje rechts van de middelste
    ed = n - 2                      # index van de laatste
    while st <= ed:                 # zolang linker index niet groter is dan rechter index
        a[st], a[ed] = a[ed], a[st]     # swap waarde rechts van center met laatste waarde
        st = st + 1
        ed = ed - 1

    for i in range(n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end=' ')
    return


test_cases = int(input())
for cs in range(test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)

"""
input:
1
7
1 2 3 4 5 6 7

output:
1 2 3 7 6 5 4

    
    def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2)
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 1
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed + 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end=' ')
    return"""