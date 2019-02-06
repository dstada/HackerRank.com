

def strangeCounter(t):
    val = 3
    while t > val:
        print("val: {}, t: {}".format(val, t))
        t = t-val
        val *= 2
        print("val: {}, t: {}".format(val, t))
    print("val: {}, t: {}".format(val, t))
    return val-t+1

# Solution which gives some time-outs:
# def strangeCounter(t):
#     value = 3
#     counter = 1
#     start_value = 3
#
#     while value >= 1 and counter < t:
#         # print("counter: {}, value: {}".format(counter, value))
#         value -= 1
#         counter += 1
#         if value == 0:
#             value = 2 * start_value
#             start_value = value
#     return value


if __name__ == '__main__':
    t = int(input())
    result = strangeCounter(t)
    print(result)

"""
https://www.hackerrank.com/challenges/strange-code/problem

Input: 4   Output: 6

1 - 3
2 - 3
3 - 1

4 - 6  <--
5 - 5
6 - 4
7 - 3
8 - 2
9 - 1

10 - 12
11 - 11
etc.
"""