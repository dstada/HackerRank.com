

def twoArrays(k, A, B):
    A.sort()
    B = sorted(B , reverse=True)
    new_list = list(zip(A, B))
    for item in new_list:
        if sum(item) < k:
            return "NO"
    return "YES"


if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])
        A = list(map(int, input().rstrip().split()))
        B = list(map(int, input().rstrip().split()))
        result = twoArrays(k, A, B)
        print(result)

"""
input:

2
3 10
2 1 3
7 8 9
4 5
1 2 2 1
3 3 3 4

output:

YES
NO


https://www.hackerrank.com/challenges/two-arrays/problem?h_r=next-challenge&h_v=zen
"""
