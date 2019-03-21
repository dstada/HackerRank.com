
def jimOrders(orders):
    orders = list(enumerate(orders))    # Maakt tuples van de list-elementen, en nummert die.
    orders = sorted(orders, key=lambda x: x[1][0] + x[1][1])    # Sorteer op de som van de twee elementen van elke tuple
    return [elem[0] + 1 for elem in orders]     # Return een list van de elementen van orders-array + 1


if __name__ == '__main__':
    n = int(input())
    orders = []
    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))
    result = jimOrders(orders)
    print(result)


"""
input:
3
1 3
2 3
3 3

output: 1 2 3
---------------------
input:
5
8 1
4 2
5 6
3 1
4 3

output:
4 2 5 1 3

https://www.hackerrank.com/challenges/jim-and-the-orders/problem
"""