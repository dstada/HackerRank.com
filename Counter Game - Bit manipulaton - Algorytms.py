

def counterGame(n):     # Louise starts first
    arr = [1, 2]
    while arr[-1]*2 <= n:
        arr.append(arr[-1]*2)
    arr = list(reversed(arr))
    teller = 0
    while n > 1:        # As long as n isn't 1
        teller += 1
        if n in arr:    # factor2
            n /= 2
        else:           # No factor2
            i = 0
            while arr[i] > n:       # As long as n > actual element
                i += 1          # Let's check next element
            n -= arr[i]         # Subtract found factor 2
    if teller % 2 == 0:         # find the player who has got a 1
        return "Richard"
    else:
        return "Louise"


if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        result = counterGame(n)
        print(result)


"""https://www.hackerrank.com/challenges/counter-game/problem

input:
1
6

output:
Richard
"""
