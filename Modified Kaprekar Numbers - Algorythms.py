

def kaprekarNumbers(p, q):
    return_string = ""
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
            return_string += str(i) + " "
        print("-----------")
    print("return_string:{}...".format(return_string))
    if return_string == "":
        return "INVALID RANGE"
    else:
        return return_string



if __name__ == '__main__':
    p = int(input())
    q = int(input())
    print(kaprekarNumbers(p, q))


"""
https://www.hackerrank.com/challenges/kaprekar-numbers/problem


input
1
100

output:

1 9 45 55 99

input:
400
700

output:
INVALID RANGE
"""