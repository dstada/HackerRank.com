from collections import Counter

def gameOfThrones(s):
    odd = 0
    for value in Counter(s).values():
        if value % 2 != 0:
            odd += 1
    if odd > 1:
        return "NO"
    else:
        return "YES"


if __name__ == '__main__':
    s = input()
    result = gameOfThrones(s)
    print(result)

"""
cdefghmnopqrstuvw --> No

cdcdcdcdeeeef --> Yes
"""