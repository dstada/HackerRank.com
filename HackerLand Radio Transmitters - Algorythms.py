# https://www.hackerrank.com/challenges/hackerland-radio-transmitters/problem


def hackerlandRadioTransmitters(x, k):
     print("Huizen op: {}".format(x))
     print("Breedte zender: {}".format(k))


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    x = list(map(int, input().rstrip().split()))
    result = hackerlandRadioTransmitters(x, k)
    print(result)

"""

5 1
1 2 3 4 5

output: 2

8 2
7 2 4 6 5 9 12 11 

output: 3

"""