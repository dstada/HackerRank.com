"""A number is called a Disarium number if the sum of the powers of its digits equals the number itself. The digits are powered to their positions in the number.

For example:
Input: 135
Output: true
135 is a Disarium number because it equals to 1^1 + 3^2 + 5^3 (each digit powered to the position in the number).
"""


def disarium_check(n):
    tot=0
    for i in range(len(n)):
        tot = tot + (int(n[i])**(i+1))
    if tot != int(n):
        return n + " isn't a disarium number..."
    else:
        return n + " is a disarium number!"


q = ""
while q not in ("N", "n", "R", "r"):
    q = input("[N]umber of [R]ange:")
if q == "N" or q == "n":
    num = input("Give number: ")
    print(disarium_check(num))
else:
    first = input("Give first number: ")
    last = input("Last number: ")
    for j in range(int(first), int(last) + 1):
        print(disarium_check(str(j)))



