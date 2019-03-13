

def balancedSums(arr):
    if sum(arr[1:]) == 0 or sum(arr[:-1]) == 0:
        return "YES"
    if len(arr) == 2:
        return "NO"
    i = 0
    j = len(arr) - 1
    links = arr[i]
    rechts = arr[j]
    tot = 2
    while tot != len(arr) - 1:
        if links < rechts:
            i += 1
            links += arr[i]
            print("links: {} - rechts: {}".format(links, rechts))
        elif links > rechts:
            j -= 1
            rechts += arr[j]
            print("links: {} - rechts: {}".format(links, rechts))
        else:       # links gelijk aan rechts
            print("Volgenden: links: {} en rechts: {}".format(arr[i+1], arr[j-1]))
            if arr[i+1] <= arr[j-1]:
                print("links minder dan rechts")
                i += 1
                links += arr[i]
                print("Links wordt nu: {} en rechts: {}".format(links, rechts))
            else:
                print("rechts minder dan links")
                j -= 1
                rechts += arr[j]
                print("links: {} - rechts: {}".format(links, rechts))
        tot += 1
    print("links: {} - rechts: {}".format(links, rechts))
    if links == rechts:

        print("gelijk! Dus YES")
    else:
        print("niet gelijk... dus NO")
    print(tot)


if __name__ == '__main__':
    T = int(input().strip())
    for T_itr in range(T):
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        result = balancedSums(arr)
        print(result)

"""
input:
10
1
1
------
1
2
------
1
3
------
2
1 2 --> NO
------
3
1 4 1
------
3
1 5 1
1
234
1
20000
3
6 23 6
1
1

output:
YES
YES
YES
NO
YES
YES
YES
YES
YES
YES

-------------
2
3
1 2 3
4
1 2 3 3

NO
YES

3
5
1 1 4 1 1
4
2 0 0 0
4
0 0 2 0 

YES
YES
YES

Case 6: (wrong but output must be YES
1
1
1

YES

https://www.hackerrank.com/challenges/sherlock-and-array/problem

Time out with case 3 and 4:

def balancedSums(arr):
    for i in range(len(arr)):
        # print(sum(arr[:i]), sum(arr[i+1:]))
        if sum(arr[:i]) == sum(arr[i+1:]):
            return "YES"
    return "NO"
"""