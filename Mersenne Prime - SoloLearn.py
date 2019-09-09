"""Mersenne Prime

A Mersenne prime is a prime number that is one less than a power of two. It is a prime number of the form 2^n − 1 for some integer n.
Input: 3
Output: true (3 is a prime number and 3=2^2-1)

Input: 31
Output: true (31 is a prime number and 31=2^5-1)

Input: 17
Output: false (17 is a prime number but it is not of the form 2^n-1)

Write a program to check if the user input is a Mersenne prime or not.

Dick STADA, Sep 2019
"""

n = int(input("Give a number: "))


# Check prime:
def check_prime(n):
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


def check_power2(n):
    for i in range(n):
        if 2 ** i == n:
            return True
    return False


def check_Mersenne(n):
    # Prime?
    if check_prime(n):
        if check_power2(n + 1):
            # print("true")
            return True
        else:
            # print("false")
            return False
    else:
        # print("false")
        return False


if check_Mersenne(n):
    print("{} is a Mersenne prime!".format(n))
else:
    print("{} is not a Mersenne prime...".format(n))