"""Leonardo loves primes and created q queries where each query takes the form of an integer, n
For each n , he wants you to count the maximum number of unique prime factors of any number in the inclusive
range [1,n] and then print this value on a new line.
"""

def primeCount(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    for i in range(n):
        count,result = 0, 1
        for j in primes:
            result *= j
            if result <= n:
                count += 1
        return count



if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        n = int(input())

        print(primeCount(n))




