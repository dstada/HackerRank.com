def luckBalance(k, contests):
    print(k)
    print(contests)
    imp = []
    unimp = []
    for cont in contests:
        if cont[1] == 1:
            imp.append(cont[0])
        else:
            unimp.append(cont[0])
    imp.sort()
    print(imp)
    unimp.sort()
    print(unimp)



    return 10



if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    contests = []
    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))
    result = luckBalance(k, contests)
    print(result)

"""6 3
5 1
2 1
1 1
8 1
10 0
5 0
Output
29
"""