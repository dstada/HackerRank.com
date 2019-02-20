

def kaprekarNumbers(p, q):

    for i in range(p, q + 1):
        som = 0
        square = str(i*i)
        print(i, square)
        # Split the square in 2 parts:
        right = square[-len(str(i)):]
        print(right)
        left = square[:(len(str(square))-len(right))]
        print("left: {}  | right: {}".format(left, right))
        if left == "":
            print("links None")
            som = int(right)
        else:
            som = int(left) + int(right)
        # else:
        #     som = int(left) + int(right)
        print("som: {}".format(som))

        if som == i:
            print("Kaprekar!")



        # print(type(int(left)))
        # tot = int(left)+int(right)
        # if tot == i:
        #     print("Kaprekar!")
        print("-----------")


if __name__ == '__main__':
    p = int(input())
    q = int(input())
    kaprekarNumbers(p, q)


"""
https://www.hackerrank.com/challenges/kaprekar-numbers/problem


input
1
100

output:

1 9 45 55 99
"""