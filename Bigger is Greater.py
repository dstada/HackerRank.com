def biggerIsGreater(w):
    print(w)
    lst = []

    for letter in w:
        print(ord(letter))
        lst.append(ord(letter))
    print(lst)


if __name__ == '__main__':
    T = int(input())
    for T_itr in range(T):
        w = input()
        result = biggerIsGreater(w)
        print(result)

"""
Input:
5
ab
bb
hefg
dhck
dkhc

Output:
ba
no answer
hegf
dhkc
hcdk


https://www.hackerrank.com/challenges/bigger-is-greater/problem?h_r=next-challenge&h_v=zen
"""