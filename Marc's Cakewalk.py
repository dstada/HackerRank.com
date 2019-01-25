

def marcsCakewalk(calorie):
    calorie.sort(reverse=True)
    cal_tot = 0
    for i in range(len(calorie)):
        cal_tot += 2**i * calorie[i]
    return cal_tot



if __name__ == '__main__':
    n = int(input())
    calorie = list(map(int, input().rstrip().split()))
    result = marcsCakewalk(calorie)
    print(result)

"""
3
1 3 2

Output: 11

https://www.hackerrank.com/challenges/marcs-cakewalk/problem
"""