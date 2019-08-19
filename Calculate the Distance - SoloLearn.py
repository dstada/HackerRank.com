"""Calculate the Distance - SoloLearn
Calculate the distance of two points on a graph, given the x and y coordinates.

Dick Stada - August 2019
"""
import math
print("Give ax, ay, bx, by, separated by a space:")

coods = list((map(int,input("").split())))

ax = coods[0]
ay = coods[1]
bx = coods[2]
by = coods[3]

d = round(((bx - ax)**2 + (by - ay)**2)**.5, 2)

print("The distance between ({},{}) and ({},{}) is {}".format(ax, ay, bx, by, d))