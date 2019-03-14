import re

def sherlockAndAnagrams(s):
    for i in range(len(s)+1):       # Make all possible combinations
        for j in range(i+1, len(s)+1):
            print(s[i:j])
            for letter in s[i:j]:
                list = []
                print("Letter: {}".format(letter))
                list = [m.start() for m in re.finditer(letter, s)]
                print(list)
                print("index: {}:{}".format(i, j))
    return ""


if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        s = input()
        result = sherlockAndAnagrams(s)
        print(result)

"""
Input:
2
ifailuhkqq
kkkk

Output 1
3
10

Input 2:
1
cdcd

Output 2
5

"""