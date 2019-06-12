"""
A number is ugly if its only prime factors are 2,3 or 5.
[1,2,3,4,5,6,8,9,10,12,15,...]

https://code.sololearn.com/cIRQWjD5Ds1a/#py
"""

n = int(input("Insert number: "))

while n % 2 == 0:
    n /= 2
while n % 3 == 0:
    n /= 3
while n % 5 == 0:
    n /= 5
if n == 1:
    print("{} is an Ugly Number!".format(int(n)))
else:
    print("{} is NOT an Ugly Number...".format(int(n)))