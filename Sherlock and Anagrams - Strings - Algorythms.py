import collections
import re


def sherlockAndAnagrams(s):
    combs = []
    anagrams = 0
    for i in range(len(s)+1):
        for j in range(i+1, len(s)+1):
            combs.append(s[i:j])

    combs_sorted = []
    for comb in combs:
        combs_sorted.append(sorted(comb))

    while len(combs_sorted) > 1:
        poss = combs_sorted.count(combs_sorted[0])
        if poss > 1:
            anagrams += int((poss*(poss-1))/2)
        combs_sorted = list(filter(combs_sorted[0].__ne__, combs_sorted))
    return anagrams


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

Input 3:
2
abba
abcd

output 3:
4
0

https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_r=internal-search

def sherlockAndAnagrams(s):
    for i in range(len(s)+1):       # Make all possible combinations
        for j in range(i+1, len(s)+1):
            # print(s[i:j])       # Deze substring bekijken
            anagram = False
            for letter in s[i:j]:       # voor elke letter kijken waar hij voorkomt
                # print("Letter: {}".format(letter))
                list = [m.start() for m in re.finditer(letter, s)]      # Indexen waar deze letter voorkomt in s
                # print("Komt voor in: {}".format(list))
                # print("index: {}:{}".format(i, j))
                list_substring = [x for x in range(i, j)]       # De indexen van de substring
                diff = set(list) - set(list_substring)          # Waar letter buiten de substring voorkomt
                if len(diff) > 0:
                    # print("komt buiten de substring voor")
                    anagram = True
                    break
                # print(diff)
            # print('==================')
    return ""

"""