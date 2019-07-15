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
right = []
print(left, right)
if n == 1:
    print("     1 >")
    print("           [1]")
    print("Total time: 1 minute")
elif n == 2:
    print("       1+2 >")
    print("             [1, 2]")
    print("Total time: 2 minutes")
else:       # n > 2
    moves = 0
    switch = []
    try:
        while len(left) > 0:
            # Two lowest from left to right side:
            if len(left) == 0:
                break
            highest = 0
            for _ in range(2):
                if min(left) >= highest:
                    highest = min(left)
                right.append(min(left))
                switch.append(min(left))
                left.remove(min(left))
            moves += highest
            print(sorted(left), ">", sorted(right), "-", highest, "minutes")
            switch = []

            # Lowest from right to left side:
            if len(left) == 0:
                break
            moves += min(right)
            lowest = min(right)
            left.append(min(right))
            right.remove(min(right))
            print(sorted(left), "<", sorted(right), "-", lowest, "minutes")

            # Two highest from left to right side:
            if len(left) == 0:
                break
            highest = 0
            for _ in range(2):
                if max(left) >= highest:
                    highest = max(left)
                right.append(max(left))
                left.remove(max(left))
            moves += highest
            print(sorted(left), ">", sorted(right), "-", highest, "minutes")

            # Lowest from right to left:
            if len(left) == 0:
                break
            moves += min(right)
            lowest = min(right)
            left.append(min(right))
            right.remove(min(right))
            print(sorted(left), "<", sorted(right), "-", lowest, "minutes")
        print("Total time: {} minutes".format(moves))
    except ValueError:
        pass