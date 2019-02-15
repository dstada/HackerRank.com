import math

def encryption(s):
    deler = int(math.sqrt(len(s)))
    woord = ""
    for j in range(deler + 1):

        for i in range(deler):
            woord += s[i * 4 + j]
        woord += " "
    print(woord)


if __name__ == '__main__':
    s = input()
    encryption(s)

"""
haveaniceday

hae and via ecy

https://www.hackerrank.com/challenges/encryption/problem
"""