

def twoPluses(grid):
    print(grid)
    max_area = 1
    for i in range(1, len(grid)-1):         # Elk cel langs die niet aan de rand zit
        for j in range(1, len(grid[0])-1):
            # Bepaal voor deze cel de grootte van de plus
            print(str(grid[i][j]))
            print(i, "-", j)
            # Bepaal hoe groot de plus maximaal kan zijn:
            min_abov_undr = min((len(grid)-int(i)-1), i)
            min_left_right = min(j, (len(grid[0])-int(j))-1)
            maximum = min(min_abov_undr, min_left_right)        # Plus kan maximaal [maximum] groot zijn.
            plusgrootte = 0
            area = 0
            for max in range(1, maximum+1):     # Hoe groot is de maximale plus
                if grid[i-max][j] == "G" and grid[i+max][j] == "G" and grid[i][j-max] == "G" and grid[i][j+max] == "G":
                    print("Extra cel!")
                    plusgrootte += 1
                    area = (4 * plusgrootte) + 1
                else:
                    break
            # print("plusgrootte: {}".format(plusgrootte))
            print("area voor deze cel: {}".format(area))
            if area > max_area:
                max_area = area
            # Nu een nieuw grid maken met huidige plus als "D" in de cellen:


            # Nu opnieuw de grootste area berekenen
            # eerste area * nieuwe grootste area onthouden.
            # Als dat bij een volgende cel groter is, wordt dat het nieuwe totaal.


            print("-----------------------------")



    print("max_area: {}".format(max_area))

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