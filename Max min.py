def maxMin(k, arr):
    arr = sorted(arr)
    unfairs = []
    for i in range(0, len(arr) -k + 1):
        temp_list = arr[i:i+k]
        unfairs.append(max(temp_list) - min(temp_list))
    return min(unfairs)


if __name__ == '__main__':
    n = int(input())
    k = int(input())
    arr = []
    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)
    print(result)

"""
https://www.hackerrank.com/challenges/angry-children/problem
10
4
1
2
3
4
10
20
30
40
100
200

Output: 3

7
3
10
100
300
200
1000
20
30

Output: 20
"""