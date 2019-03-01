

def gridSearch(G, P):       # G = grote matrx en P is de kleine die gezocht moet worden
    # if P[0] in G[0]:
    #     print("ja")
    # else:
    #     print("no")
    # Zoek de eerste regel van G waarin de eerste regel van P zit.
    # Niet aanwezig? Output is NO.
    for i in range(len(G) - (len(P) - 1)):
        print(i)
        try:
            start_index = G[i].index(P[0])
            print("1e regel komt voor")
            # Eerste regel komt voor; nu de andere regels checken:
            for j in range(len(P) - 1):     # voor alle regels van P behalve de eerste

        except ValueError:
            print("Niet in deze regel...")

    if start_index:
        print("jawel")
    else:
        print("Niet aanwezig")




if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        RC = input().split()
        R = int(RC[0])
        C = int(RC[1])
        G = []
        for _ in range(R):
            G_item = input()
            G.append(G_item)
        rc = input().split()
        r = int(rc[0])
        c = int(rc[1])
        P = []
        for _ in range(r):
            P_item = input()
            P.append(P_item)
        result = gridSearch(G, P)
        print(result)

"""https://www.hackerrank.com/challenges/the-grid-search/problem?h_r=next-challenge&h_v=zen
Input:

2
10 10
7283455864
6731158619
8988242643
3830589324
2229505813
5633845374
6473530293
7053106601
0834282956
4607924137
3 4
9505
3845
3530
15 15
400453592126560
114213133098692
474386082879648
522356951189169
887109450487496
252802633388782
502771484966748
075975207693780
511799789562806
404007454272504
549043809916080
962410809534811
445893523733475
768705303214174
650629270887160
2 2
99
99

Output:

YES
NO

------------------
1
10 10
7283455864
6731158619
8988242643
3830589324
2229505813
5633845374
6473530293
7053106601
0834282956
4607924137
3 4
4558
3845
3530
"""