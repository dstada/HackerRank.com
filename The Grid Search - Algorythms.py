

def gridSearch(G, P):       # G = grote matrix en P is de kleine die gezocht moet worden
    # Zoek in G regel voor regel of de eerste regel van P erin zit.
    start_index = -1
    uitslag = "NO"
    for i in range(len(G) - (len(P) - 1)):  
        try:
            start_index = G[i].index(P[0])
            print("1e regel van P komt voor in regel {} van G, vanaf plek {}".format(i, start_index))
            zelfde = 1
            for j in range(1, len(P)):     # Check alle regels van P behalve de eerste
                print("Check van G: {} of regel {} van P erin zit.".format(G[j + i], P[j]))
                # print("Nu in P de te checken regel: {}".format(P[j]))
                print(G[j+i][start_index:start_index + len(P) + 1])
                if G[j+i][start_index:start_index + len(P) + 1] == P[j]:
                    print("Deze regel is ook hetzelfde!")
                    zelfde += 1
                    if zelfde == len(P):
                        print("Alle {} regels in P gevonden".format(zelfde))
                        return "YES"
                else:
                    print("Deze regel is niet hetzelfde...")
                    break

        except ValueError:
            pass
    return uitslag


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
Alleen in regel 0, dus NO:
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
-------------------
Yes, want vanaf regel 4:
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
9505
3845
3530

1e regel niet aanwezig, dus NO:

1
10 10
7283455864
6731158619
8988242643
3830589324
2229506813
5633845374
6473530293
7053106601
0834282956
4607924137
3 4
9505
3845
3530

1
4 6
123412
561212
123634
781288
2 2
12
34
------------------------
1
25 25
7652157548860692421022503
9283597467877865303553675
4160389485250089289309493
2583470721457150497569300
3220130778636571709490905
3588873017660047694725749
9288991387848870159567061
4840101673383478700737237
8430916536880190158229898
8986106490042260460547150
2591460395957631878779378
1816190871689680423501920
0704047294563387014281341
8544774664056811258209321
9609294756392563447060526
0170173859593369054590795
6088985673796975810221577
7738800757919472437622349
5474120045253009653348388
3930491401877849249410013
1486477041403746396925337
2955579022827592919878713
2625547961868100985291514
3673299809851325174555652
4533398973801647859680907
5 4
5250
1457
8636
7660
7848


---------------------
1
5 15
111111111111111
111111111111111
111111111111111
111111111111111
111111111111110
3 5
11111
11111
11110
"""