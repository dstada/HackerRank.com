

def gemstones(arr):
    print(arr)
    mylist = [set(i) for i in arr]  # list van sets (met unieke waarden erin)
    # print(mylist)
    temp = mylist[0].intersection(mylist[1])
    for i in range(len(mylist) - 2):
        temp = temp.intersection(mylist[i+2])
    # print(temp)
    return len(temp)


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
"""