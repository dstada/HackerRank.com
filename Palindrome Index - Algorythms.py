

def palindromeIndex(s):
    print(s)
    print(s[::-1])
    if s == s[::-1]:
        return -1
    else:
        for i in range(len(s)+1):
            if i > 0:
                s_temp = s[:i-1] + s[i:]
                print(s_temp)

                if s_temp == s_temp[::-1]:
                    print("Nu wél palindroom!")
                    return i-1


if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        s = input()
        result = palindromeIndex(s)
        print(result)


"""
Input:
3
aaab
baa
aaa

Output:
3
0
-1

Inputs:
abcba

cwwcw

wcwwc

hgygsvlfcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcwflvsgygh

https://www.hackerrank.com/challenges/palindrome-index/problem
"""