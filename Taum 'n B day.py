def taumBday(b, w, bc, wc, z):
    # b = aantal black gifts
    # w = aantal witte gifts
    # bc = prijs van b
    # wc = prijs van w
    # z = kosten van w naar b en andersom
    return b * min(bc, wc + z) + w * min(wc, bc + z)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        bw = input().split()

        b = int(bw[0])

        w = int(bw[1])

        bcWcz = input().split()

        bc = int(bcWcz[0])
        wc = int(bcWcz[1])
        z = int(bcWcz[2])

        result = taumBday(b, w, bc, wc, z)
        print(result)

"""
5
10 10
1 1 1
5 9
2 3 4
3 6
9 1 1
7 7
4 2 1
3 3
1 9 2
Output: 
20
37
12
35
12
"""