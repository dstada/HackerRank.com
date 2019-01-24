

def wrapper(f):
    def fun(l):
        # complete the function
    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)


"""
3
07895462130
919875641230
9195969878
Sample Output

+91 78954 62130
+91 91959 69878
+91 98756 41230

https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem
"""