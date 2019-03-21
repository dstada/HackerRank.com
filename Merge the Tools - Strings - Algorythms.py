

def merge_the_tools(s, k):
    for i in range(0, len(s), k):
        sub = s[i:i+k]
        outpt = ""
        for letter in sub:
            if letter not in outpt:
                outpt += letter
        print(outpt)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


"""
Input:
AABCAAADA
3

Output:
AB
CA
AD

https://www.hackerrank.com/challenges/merge-the-tools/problem
"""