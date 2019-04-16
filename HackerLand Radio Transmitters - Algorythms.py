# https://www.hackerrank.com/challenges/hackerland-radio-transmitters/problem
# Medium | Score: 25


def hackerlandRadioTransmitters(x, k):
    x.sort()
    transmitters = 0
    lasthouse = 0
    for house in x:
        if house > lasthouse:   # huidige huis verder dan bereik van transmitter
            transmitters += 1   # aantal transmitters wort groter
            # print("transmitters nu: {}".format(transmitters))
            lasthouse = house + 2 * k   # bereik transmitter schuift nu op
    return transmitters


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