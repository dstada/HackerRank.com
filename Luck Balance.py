def luckBalance(k, contests):
    contests.sort(reverse=True)
    luck = 0
    imp = 0

    for cont in contests:
        if cont[1] == 0:    # An important contest
            luck += cont[0]
        elif imp < k:       # An  unimportant contest, if nr of imp. contests < k
            luck += cont[0] # luck grows
            imp += 1        # imp grows
        else:
            luck -= cont[0] # Unimportant contest and imp less than k

    return luck



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

# Not for all cases right:

def luckBalance(k, contests):
    # imp = []
    # unimp = []
    # for cont in contests:
    #     if cont[1] == 1:
    #         imp.append(cont[0])
    #     else:
    #         unimp.append(cont[0])
    # imp.sort()
    # print(imp)
    # unimp.sort()
    # print(unimp)
    # # print(sum(imp[-k:])+sum(unimp))
    # # print(sum(imp[:len(imp)-k]))
    # return sum(imp[-k:])+sum(unimp) - sum(imp[:len(imp)-k])
"""