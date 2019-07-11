"""
[CHALLENGE] CROSSING THE BRIDGE

Write a program to print the minimum time taken to get N people from one side of a bridge to the other if
a) The bridge can only hold two people at a time.
b) It's dark and the only flashlight must be carried while crossing.
c) People are numbered from 1 to N. The k-th person takes k minutes to cross the bridge.
d) A pair crosses at the speed of the slowest member.

For example:
Input: 4
Output: 11

1&3 cross (time 3), 1 returns (1)
1&4 cross (4), 1 returns (1)
1&2 cross (2)
3 + 1 + 4 + 1 + 2 = 11

BONUS: Print who crosses/returns at each step.
"""


n = int(input("People: "))
left = []
for i in range(n):
    left.append(i+1)
print(left)
right = []
if n == 1:
    print("Crossing: 1")
elif n == 2:
    print("Crossing: 1+2")
else:       # n > 2
    # while len(left) > 0:
    #     # Laagste twee van links naar rechts:
    #     for _ in range(2):
    #         right.append(min(left))
    #         left.remove(min(left))
    #     # Laagste van rechts naar links:
    #     left.append(min(right))
    #     right.remove(min(right))
    #     # Hoogste twee van links naar rechts:
    #     for _ in range(2):
    #         right.append(max(left))
    #         left.remove(max(left))
    #     # Laagste van links naar rechts:
    #     left.append(min(right))
    #     right.remove(min(right))
    moves = 0
    try:
        while len(left) > 0:
            # Laagste twee van links naar rechts:
            for _ in range(2):
                right.append(min(left))
                left.remove(min(left))
                moves += 1
            # Laagste van rechts naar links:
            left.append(min(right))
            right.remove(min(right))
            moves += 1
            # Hoogste twee van links naar rechts:
            for _ in range(2):
                right.append(max(left))
                left.remove(max(left))
                moves += 1
            # Laagste van links naar rechts:
            left.append(min(right))
            right.remove(min(right))
            moves += 1
    except ValueError:
        print("Moves: {}".format(moves))
print(left, right)