def separateNumbers(s):




if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)

"""
https://www.hackerrank.com/challenges/separate-the-numbers/problem?h_r=next-challenge&h_v=zen

Input:
7
1234
91011
99100
101103
010203
13
1

Output:
YES 1
YES 9
YES 99
NO
NO
NO
NO
"""