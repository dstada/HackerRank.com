def bigSorting(unsorted):
    return sorted(sorted(unsorted), key=len)

if __name__ == '__main__':
    n = int(input())
    unsorted = []
    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)
    result = bigSorting(unsorted)
    print(result)