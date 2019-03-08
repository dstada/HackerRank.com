

def anagram(s):
    if len(s) % 2 != 0:     # length s odd, so no anagram possible
        return -1
    firstpart, secondpart = s[:len(s)//2], s[len(s)//2:]
    for i in range(len(firstpart)):
        if firstpart[i] in secondpart:
            ind = secondpart.index(firstpart[i])
            secondpart = secondpart[:ind] + secondpart[ind+1:]
    return len(secondpart)



if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        s = input()
        result = anagram(s)
        print(result)

"""
https://www.hackerrank.com/challenges/anagram/problem

input:

6
aaabbb
ab
abc
mnop
xyyx
xaxbbbxx

output:

3
1
-1
2
0
1
"""