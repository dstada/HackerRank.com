import collections

def rotLeft(a, d):
    a_deque = collections.deque(a)
    for i in range(d):
        a_deque.append(a_deque[0])
        a_deque.popleft()
    print(a_deque)


if __name__ == '__main__':
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    a = list(map(int, input().rstrip().split()))
    result = rotLeft(a, d)
    print(result)


"""
Sample Input
5 4
1 2 3 4 5

Sample Output
5 1 2 3 4
"""