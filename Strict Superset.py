A = set(list(map(int, input().split())))
superset = False

for i in range(int(input())):
    B = set(map(int, input().split()))
    if A.issuperset(B):
        superset = True
    else:
        superset = False
        break

print(superset)


"""

1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12

Output:
False


for i in range(int(input())):
    B = set(map(int, input().split()))
    len_A = len(A)
    len_B = len(B)

    # print(B)
    # Kijk wat overbllijft van A als B eraf wordt getrokken:
    A.difference_update(B)
    # print(A)
    # print(len(A))
    if len(A) > 0 and len(A) + len_B == len_A:
        superset = True
    else:
        superset = False
        break

"""