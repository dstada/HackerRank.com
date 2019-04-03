

def solve(n):
    arr = []
    for i in range(50):
        if i == 0:
            arr.append(0)
        elif i == 1:
            arr.append(1)
        else:
            arr.append(arr[i-1] + arr[i - 2])
    print(arr)
    if n in arr:
        return "IsFibo"
    else:
        return "IsNotFibo"


if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        result = solve(n)
        print(result)

"""
input:
3
5
7
8

output:
IsFibo
IsNotFibo
IsNotFibo


def CheckPerfect(x):
    i = int(math.sqrt(x))
    return (x == i*i)


def CheckFibo(n):
    if CheckPerfect(5*n*n + 4) or CheckPerfect(5*n*n - 4):
        print("Fibonacci")
    else:
        print("Not Fibonacci")

# CheckFibo(89) #this returns true, 89 is Fibonacci

https://www.hackerrank.com/challenges/is-fibo/forum

"""