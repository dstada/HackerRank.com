"""
5 6
GGGGGG
GBBBGB
GGGGGG
GGBBGB
GGGGGG

"""

def twoPluses(grid):
    if not any("G" in rule for rule in grid):   # if no G's in the grid, return 0
        return 0
    # max_area = 1
    for i in range(1, len(grid)-1):         # Elk cel langs die niet aan de rand zit
        for j in range(1, len(grid[0])-1):
            grid_new = grid.copy()
            if grid[i][j] == "G":
                print("Grid: {}".format(grid))
                grid_new[i] = grid_new[i][:j] + "B" + grid_new[i][j + 1:]   # De cel zelf van G naar B
                # Bepaal voor deze cel de grootte van de plus
                print(i, "-", j)
                # Bepaal hoe groot de plus maximaal kan zijn (theoretische plusgrootte):
                min_abov_undr = min((len(grid)-int(i)-1), i)
                min_left_right = min(j, (len(grid[0])-int(j))-1)
                maximum = min(min_abov_undr, min_left_right)        # Plus kan maximaal [maximum] groot zijn.
                plusgrootte = 0
                area = 0
                print(grid_new[i])
                for max in range(1, maximum+1):     # Hoe groot is de maximale plus
                    if grid[i-max][j] == "G" and grid[i+max][j] == "G" and grid[i][j-max] == "G" and grid[i][j+max] == "G":
                        # De G's veranderen in B's:
                        grid_new[i-max] = grid_new[i-max][:j] + "B" + grid_new[i-max][j+1:]    # cel boven bewuste cel
                        grid_new[i+max] = grid_new[i+max][:j] + "B" + grid_new[i-max][j+1:]    # cel onder bewuste cel
                        grid_new[i] = grid_new[i][:j - max] + "B" + grid_new[i][j - max + 1:]  # cel links
                        grid_new[i] = grid_new[i][:j + max] + "B" + grid_new[i][j + max + 1:]  # cel rechts
                        plusgrootte += 1
                        area = (4 * plusgrootte) + 1
                    else:
                        break                     # Stoppen want maximale plus bereikt
                print("Bij deze plus is de area: {}".format(area))
                print("gr_n: {}".format(grid_new))

                # Met het nieuwe grid waar de plus op de cel gemarkeerd is als "B", opnieuw de grootste plus zoeken:
                for i in range(1, len(grid_new) - 1):  # Elk cel langs die niet aan de rand zit
                    for j in range(1, len(grid_new[0]) - 1):
                        if grid_new[i][j] == "G":
                            print(grid_new[i][j])


                # Bereken area eerste keer tweede area

                # if area > max_area:
                #     max_area = area

                print("-----------------------------")
    # print("max_area: {}".format(max_area))

# TODO: Als er alleen G's in de randcellen zitten: check of er 2 G's in zitten. Return is dan 1
"""
def twoPluses(grid):
    # max_area = 1
    grid_new = grid
    for i in range(1, len(grid)-1):             # Elk regel langs
        for j in range(1, len(grid[0])-1):      # Elke letter van de regel
            if grid[i][j] == "G":
                print("Grid: {}".format(grid))
                # grid_new = ['GGGGGG', 'GGGGGG', 'GGGGGG', 'GGGGGG', 'GGGGGG']
                # grid_new[i] = grid_new[i][:j] + "B" + grid_new[i][j + 1:]
                grid_new[i] = grid[i][:j] + "B" + grid[i][j + 1:]
                print("gr_n: {}".format(grid_new))
                # Bepaal voor deze cel de grootte van de plus
                # print(str(grid[i][j]))
                # print(i, "-", j)
                # Bepaal hoe groot de plus maximaal kan zijn:
                # min_abov_undr = min((len(grid)-int(i)-1), i)
                # min_left_right = min(j, (len(grid[0])-int(j))-1)
                # maximum = min(min_abov_undr, min_left_right)        # Plus kan maximaal [maximum] groot zijn.
                # plusgrootte = 0
                # area = 0
                # grid_new[i] = grid_new[i][:j] + "B" + grid_new[i][j + 1:]  # de cel zelf (is dat wel nodig?)
                # print(grid_new[i])
                # for max in range(1, maximum+1):     # Hoe groot is de maximale plus
                #     if grid[i-max][j] == "G" and grid[i+max][j] == "G" and grid[i][j-max] == "G" and grid[i][j+max] == "G":
                #         print("Extra cel!")
                #         # De G's veranderen in B's:
                #         grid_new[i-max] = grid_new[i-max][:j] + "B" + grid_new[i-max][j+1:]    # cel boven bewuste cel
                #         grid_new[i+max] = grid_new[i+max][:j] + "B" + grid_new[i-max][j+1:]    # cel onder bewuste cel
                #         grid_new[i] = grid_new[i][:j - max] + "B" + grid_new[i][j - max + 1:]  # cel links
                #         grid_new[i] = grid_new[i][:j + max] + "B" + grid_new[i][j + max + 1:]  # cel rechts
                #         plusgrootte += 1
                #         area = (4 * plusgrootte) + 1
                #     else:
                #         break
                # print("Bij deze plus is de area: {}".format(area))
                # print(grid_new)
                # if area > max_area:
                #     max_area = area
                # Nu een nieuw grid maken met huidige plus als "D" in de cellen:
                # Neem cel voor cel over uit oorspronkelijke grid. Als cel in plus: maak een "B"


                # Nu opnieuw de grootste area berekenen
                # eerste area * nieuwe grootste area onthouden.
                # Als dat bij een volgende cel groter is, wordt dat het nieuwe totaal.
                print("-----------------------------")
    # print("max_area: {}".format(max_area))
"""

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

5 6
BBBBBB
BBBBBB
BBBBBB
BBBBBB
BBBBBB
BBBBBB

5 6
BBBGBB
BBBGBB
BGGGGG
BBBGBB
BBBGBB
BBBBBB

"""