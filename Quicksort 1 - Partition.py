def quickSort(rijtje):
    left = []
    equal = []
    right = []
    eerste = rijtje[0]
    for cijfer in rijtje:
        if cijfer < eerste:
            left.append(cijfer)
        elif cijfer == eerste:
            equal.append(cijfer)
        else:
            right.append(cijfer)
    new = left + equal + right
    return ' '.join(str(e) for e in new)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = quickSort(arr)
    print(result)

"""
https://www.hackerrank.com/challenges/quicksort1/problem?h_r=next-challenge&h_v=zen

5
4 5 3 7 2

Output: 3 2 4 5 7
"""