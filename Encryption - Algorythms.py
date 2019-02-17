import math

def encryption(s):
    if int(math.sqrt(len(s))) * int(math.sqrt(len(s))) == len(s):
        deler_hor = int(math.sqrt(len(s)))
        deler_ver = int(math.sqrt(len(s)))
    else:
        deler_hor = int(math.sqrt(len(s))) + 1

    if deler_hor * (deler_hor - 1) < len(s):
        deler_ver = deler_hor
    else:
        deler_ver = deler_hor - 1

    woord = ""
    for j in range(deler_hor):
        for i in range(deler_ver):
            try:
                woord += s[j + i * (deler_hor)]
            except IndexError:
                woord += ""

        woord += " "
    return woord


if __name__ == '__main__':
    s = input()
    encryption(s)
    print(encryption(s))

"""
haveaniceday --> hae and via ecy

feedthedog --> fto ehg ee dd

chillout --> clu hlt io

chilloutx --> clu hlt iox

ifmanwasmeanttostayonthegroundgodwouldhavegivenusroots -->
imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau

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