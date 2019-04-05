
import math


def is_smart_number(num):
    val = int(math.sqrt(num))
    if val * val == num:
        return True
    return False


for _ in range(int(input())):
    num = int(input())
    ans = is_smart_number(num)
    if ans:
        print("YES")
    else:
        print("NO")


"""
https://www.hackerrank.com/challenges/smart-number/problem

input:
4
1
2
7
169

output:
YES
NO
NO
YES

--------------------------------------
    val = int(math.sqrt(num))
    if num / val == 1:
        return True
    return False
---------------------------------------

def is_smart_number(num):
    teller = 0
    for i in range(1, num + 1):
        if num % i == 0:
            teller += 1
    if teller % 2 == 0:
        return False
    else:
        return True

for _ in range(int(input())):
    num = int(input())
    print(is_smart_number(num))
"""