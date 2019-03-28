"""
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    k0 = 6*n % 15
    k = k0 + 15*((n-k0)//15)
    print( "-1" if k0 > n else k*"5" + (n-k)*"3" )
"""


def decentNumber(n):
    if n < 3:               # n moet 3 of meer zijn
        return -1
    elif n % 3 == 0:        # n deelbaar door 3
        return int((n / 3)) * "555"
    elif n % 5 == 0 and n >= 5:        # n deelbaar door 5
        return int((n / 5)) * "33333"
    elif n >= 8:            # niet deelbaar door 3 of 5
        # Eerst alle posities vullen met 5'en
        # bijv. 11 --> 55555555555
        for i in range(1, n//5 + 1):
            # Vul op vanaf rechts met steeds 5 x een 3, en check of rest deelbaar is door 3:
            if (n - i * 5) % 3 == 0:    # Als van n x keer 5 3'en afgaan, is dan de rest deelbaar door 5?
                outpt = ((n - i * 5) // 3) * "555" + i * "33333"
                return outpt
                break
    else:
        return -1


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        print(decentNumber(n))


"""https://www.hackerrank.com/challenges/sherlock-and-the-beast/problem

input:
4
1
3
5
11

output
-1
555
33333
55555533333
"""