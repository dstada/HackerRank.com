"""Leonardo loves primes and created q queries where each query takes the form of an integer, n
For each n , he wants you to count the maximum number of unique prime factors of any number in the inclusive
range [1,n] and then print this value on a new line.
"""


def check_prime(n):      # checks is n is a prime
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6
    return True


def primeCount(n):
    number_of_primes = 0
    total = 0
    for i in range(3, n//2):
        if check_prime(i):
            print(i)
            if total == 0:
                total = i
            else:
                total *= i
            print("total: {}".format(total))
            number_of_primes += 1
            print("nr of primes: {}".format(number_of_primes))
            if total > n:
                return number_of_primes - 1



if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        n = int(input())

        print(primeCount(n))




