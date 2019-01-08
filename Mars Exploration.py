def marsExploration(st):
    print(st)
    fout = 0
    for i in range(len(st)):
        if (i + 1) % 3 == 1 or (i + 1) % 3 == 0:
            if st[i] != "S":
                fout += 1
        else:
            if st[i] != "O":
                fout += 1
    return fout



if __name__ == '__main__':
    s = input()
    result = marsExploration(s)


"""
SOSSPSSQSSOR --> 3

SOSSOT --> 1

https://www.hackerrank.com/challenges/mars-exploration/problem
"""