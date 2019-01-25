# from fractions import Fraction
#
# oupt = Fraction(16, -10)
# print(oupt[0])
# print(list(oupt).split('/'))


from fractions import Fraction
from functools import reduce


def product(fracs):
    t = reduce(lambda x, y : x * y, fracs)
    return t.numerator, t.denominator


if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)



