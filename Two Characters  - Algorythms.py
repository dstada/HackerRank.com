
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
    print(s)
    s_set = list(set(s))    # list of unique letters out of s
    # Make a list of all combiations of the elements except 2:
    combs = list(itertools.combinations(s_set, len(s_set) - 2))

    temp = list(filter((s_set[0]).__ne__, s))
    max_len = 0
    maxi = 0
    for comb in combs:
        temp_s = s
        print("{} eruit".format(comb))
        for j in range(len(comb)):
            temp_s = list(filter((comb[j]).__ne__, temp_s))
        print("Blijft over: {}".format(temp_s))
        # check of overgebleven letters om en om zijn:
        first = temp_s[0]
        temp_lst = []
        for x in range(0,len(temp_s), 2):
            temp_lst.append(temp_s[x])
        print(first, temp_lst)
        if len(set(temp_lst)) > 1:
            pass
        else:
            if len(temp_s) > maxi:
                maxi = len(temp_s)
                print("Max nu: {}".format(maxi))
    print(maxi)


    return "OK"



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
"""