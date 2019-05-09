"""The Collatz conjecture (also known as the Ulam conjecture or the Syracuse problem) is an unsolved mathematical problem, which is very easy to formulate:

1. Take any natural number
2. If it's even, half it, otherwise triple it and add one
3. Repeat step 2. until you reach 4, 2, 1 sequence
4. You will ALWAYS reach 1, eventually.

Dick STADA - May 2019
"""


nr = int(input("Give natural number: "))
steps = 0
while nr != 1:
    if nr % 2 == 0:
        print("{} / 2 = {}".format(nr, int(nr / 2)))
        nr = int(nr // 2)
    else:
        print("{} * 3 + 1 = {}".format(nr, int(nr * 3 + 1)))
        nr = int(nr * 3 + 1)
    steps += 1
print("Reached in {} steps.".format(steps))
