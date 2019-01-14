def gemstones(arr):
    print(arr)
    mylist = [set(i) for i in arr]
    print(mylist)
    temp = mylist[0].intersection(mylist[1])
    temp = temp.intersection(mylist[2])
    print(temp)


if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)
    result = gemstones(arr)
    print(result)

"""
Input:
3
abcdde
baccd
eeabg

Output: 2

Not working for all cases:

def gemstones(arr):
    gems = []
    for letter in arr[0]:
        total = True
        for i in range(1, len(arr)):
            if letter not in arr[i]:
                total = False
        if total is True:
            gems.append(letter)
    return len(gems)

"""