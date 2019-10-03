def twoPluses(grid):
    print(grid)
    plusses = []
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[0])-1):
            print(str(grid[i][j]))
            print(i,",",j)
            # Bepaal hoe groot de plus maximaal kan zijn:
            min_abov_undr = min((len(grid)-int(i)-1), i)
            min_left_right = min(j, (len(grid[0])-int(j))-1)
            maximum = min(min_abov_undr,min_left_right)
            print("Plus kan maximaal {} cel(len) rond centrale cel groot zijn".format(maximum))
            if grid[i][j] == "B":
                print("Foute cel...")
            else:
                print("Dit is een goede cel.")
            print("-----------------------------")

            # for k in range(1, maximum):
            #     if grid[i][j-k] == "B":
            #         print("Links is BAD")


if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)
    print(result)

"""
https://www.hackerrank.com/challenges/two-pluses/problem?h_r=next-challenge&h_v=zen

Find the two largest valid pluses that can be drawn on good cells in the grid, and return an integer denoting
the maximum product of their areas. In the above diagrams, our largest pluses have areas of 5 and 9. 
The product of their areas is 5 x 9 = 45.
Note: The two pluses cannot overlap, and the product of their areas should be maximal.
Function Description
Complete the twoPluses function in the editor below. It should return an integer that represents the area
of the two largest pluses.

input:

5 6
GGGGGG
GBBBGB
GGGGGG
GGBBGB
GGGGGG

output: 
5

input:
6 6
BGBBGB
GGGGGG
BGBBGB
GGGGGG
BGBBGB
BGBBGB

output:
25

"""