

def toys(w):
    w = list(set(w))
    i = 0
    containers = 0
    while i < len(w):
        unit = []
        unit.append(w[i])
        if max(unit) - min(unit) <= 4:
            i += 1
        else:
            units += 1
            break
    print(units)



if __name__ == '__main__':
    n = int(input())
    w = list(map(int, input().rstrip().split()))
    result = toys(w)
    print(result)


"""
https://www.hackerrank.com/challenges/priyanka-and-toys/problem

Input:
8
1 2 3 21 7 12 14 21

Output:
4

Input:
1 2 3 4 5 10 11 12

Output:
2

"""