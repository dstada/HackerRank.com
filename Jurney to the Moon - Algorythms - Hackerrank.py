"""
The member states of the UN are planning to send  people to the moon. They want them to be from different countries.
You will be given a list of pairs of astronaut ID's.'
                                                                                                                                                                      ' Each pair is made of astronauts from the same country. Determine how many pairs of astronauts from different countries they can choose from.
# Complete the journeyToMoon function below.

The first line contains two integers n and p, the number of astronauts and the number of pairs.
Each of the next p lines contains 2 space-separated integers denoting astronaut ID's of two who share the same nationality.
"""

def journeyToMoon(n, astronaut):
    print(n, astronaut)
    


if __name__ == '__main__':
    np = input().split()
    n = int(np[0])
    p = int(np[1])
    astronaut = []
    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

"""
Sample Input:

5 3
0 1
2 3
0 4

Output:
6
"""