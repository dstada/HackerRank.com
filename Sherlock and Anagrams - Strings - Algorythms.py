import re

def sherlockAndAnagrams(s):
    combs = []
    for i in range(len(s)+1):       # Make all possible combinations
        for j in range(i+1, len(s)+1):
            print(s[i:j])       # Deze substring bekijken
            combs.append(s[i:j])
    print(combs)
    for i in range(len(combs) - 1):
        if sorted(combs[i]) == sorted(combs[i+1]):
            print("Gelijk")
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


def sherlockAndAnagrams(s):
    for i in range(len(s)+1):       # Make all possible combinations
        for j in range(i+1, len(s)+1):
            print(s[i:j])       # Deze substring bekijken
            anagram = False
            for letter in s[i:j]:       # voor elke letter kijken waar hij voorkomt
                print("Letter: {}".format(letter))
                list = [m.start() for m in re.finditer(letter, s)]      # Indexen waar deze letter voorkomt in s
                print("Komt voor in: {}".format(list))
                print("index: {}:{}".format(i, j))
                list_substring = [x for x in range(i, j)]       # De indexen van de substring
                diff = set(list) - set(list_substring)          # Waar letter buiten de substring voorkomt
                if len(diff) > 0:
                    print("komt buiten de substring voor")
                    anagram = True
                    break
                print(diff)
            print('==================')
    return ""

"""