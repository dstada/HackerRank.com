"""
SoloLearn - Strange Root

A number has a strange root if its square and square root share any digit:
Input: 11
Square = 121
Square root (3 decimals) = 3.317
Both have a 1, so strange root.
"""

n = input("Give a number: ")
if any(x in str(int(n)**2) for x in str(round(int(n)**.5, 3))):         # iets uit n_sq in n_sqrt?
    print("{} is a Strange Root!".format(n))
else:
    print("{} is not a strange root".format(n))