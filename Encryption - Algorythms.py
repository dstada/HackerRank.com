import math

def encryption(s):
    deler = int(math.sqrt(len(s)))
    print("deler: {}".format(deler))
    woord = ""
    for j in range(deler + 1):      # 0, 1, 2
        for i in range(deler):
            print("s: {} - {}".format(len(s), j + i*(deler+1)))
            try:
                woord += s[j + i * (deler + 1)]
                print("woord nu: ".format(woord))
            except IndexError:
                woord += ""

        woord += " "
    print(woord)


if __name__ == '__main__':
    s = input()
    encryption(s)

"""
haveaniceday --> hae and via ecy

feedthedog --> fto ehg ee dd

chillout --> clu hlt io


https://www.hackerrank.com/challenges/encryption/problem

def encryption(s):
    deler = int(math.sqrt(len(s)))
    print(deler)
    woord = ""
    for j in range(deler + 1):      # van 0 t/m 3 = 0, 1, 2, 3
        for i in range(deler):      # van 0 t/m 2 = 0, 1, 2
            print("s: {} - {}".format(len(s), j + i*(deler+1)))
            if j + i*(deler+1) < len(s):
                woord += s[j + i*(deler+1)]   # 0+0*4, 0+1*4, 0+2*4, 1+0*4, 1+2*4, ...
        woord += " "
    print(woord)
"""