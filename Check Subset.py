for i in range(int(input())):
    n_A = int(input())
    A = set(list(map(int, input().split())))
    n_B = int(input())
    B = set(list(map(int, input().split())))
    A.difference_update(B)
    if len(A) > 0:
        print("False")
    else:
        print("True")

