

def balancedSums(arr):
    i = 0
    j = len(arr) - 1
    while i + j




if __name__ == '__main__':
    T = int(input().strip())
    for T_itr in range(T):
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        result = balancedSums(arr)
        print(result)

"""
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
"""