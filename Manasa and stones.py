import itertools

def stones(n, a, b):
    list_combs = list(itertools.combinations_with_replacement((a, b), n-1))
    return sorted(set([sum(i) for i in list_combs]))



if __name__ == '__main__':
    T = int(input())        # aantal testcases

    for T_itr in range(T):
        n = int(input())
        a = int(input())
        b = int(input())
        result = stones(n, a, b)
        print(result)


"""
input:
2
3
1
2
4
10
100
"""