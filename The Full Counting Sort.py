def countSort(arr):



if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(input().rstrip().split())
    countSort(arr)

"""
https://www.hackerrank.com/challenges/countingsort4/problem?h_r=next-challenge&h_v=zen
Input:
20
0 ab
6 cd
0 ef
6 gh
4 ij
0 ab
6 cd
0 ef
6 gh
0 ij
4 that
3 be
0 to
1 be
5 question
1 or
2 not
4 is
2 to
4 the

Output: - - - - - to be or not to be - that is the question - - - -

"""