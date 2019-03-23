


def toys(w):
    w.sort()
    for i in range(len(w)):
        teller = 1
        min = w[i]
        if w[i+1] - w[i] <= 4 and teller <= 4:




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