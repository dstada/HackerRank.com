
# Two Characters - Algorythms
#
# In this challenge, you will be given a string. You must remove characters until the string
# is made up of any two alternating characters. When you choose a character to remove,
# all instances of that character must be removed. Your goal is to create the longest string possible
# that contains just two alternating letters.
#
# Dick Stada - March 2019
import itertools


def alternate(s):
    if len(s) == 1:
        return 0
    s_set = list(set(s))    # list of unique letters out of s
    if len(s_set) == 1:
        return 0
    # Make a list of all combinations of the elements except 2:
    combs = list(itertools.combinations(s_set, len(s_set) - 2))
    maxi = 0
    for comb in combs:
        temp_s = s
        # Haal letters eruit:
        for j in range(len(comb)):
            temp_s = list(filter((comb[j]).__ne__, temp_s))
        print("Blijft over: {}".format(temp_s))
        # check of overgebleven letters om en om zijn:
        temp_lst = []       # alle oneven elementen
        temp_lst2 = []      # alle even elementen
        for x in range(0, len(temp_s), 2):
            temp_lst.append(temp_s[x])
        for y in range(1, len(temp_s), 2):
            temp_lst2.append(temp_s[y])
        if len(set(temp_lst)) == 1 and len(set(temp_lst2)) == 1:
            if len(temp_s) > maxi:
                maxi = len(temp_s)
                print("Max nu: {}".format(maxi))
    return maxi


if __name__ == '__main__':
    l = int(input().strip())
    s = input()
    result = alternate(s)
    print(result)


"""https://www.hackerrank.com/challenges/two-characters/problem

input:
10
beabeefeab

output:
5

input:

aaaabbbbcccc --> 0

aaaabababbbb --> 0

cccccccccccc --> 0


"""