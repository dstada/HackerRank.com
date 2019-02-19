

def kaprekarNumbers(p, q):
    for i in range(p,q + 1):
        square = str(i*i)
        print(i, square)

        tot = 0
        for digit in square:
            print(digit)
            tot += int(digit)
        print(tot)
        if tot == i:
            print("kaprekar!")
        print("-----------")


if __name__ == '__main__':
    p = int(input())
    q = int(input())
    kaprekarNumbers(p, q)