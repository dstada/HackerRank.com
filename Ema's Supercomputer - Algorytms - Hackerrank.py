"""
5 6
GGGGGG
GBBBGB
GGGGGG
GGBBGB
GGGGGG

"""

def twoPluses(grid):
    max_area = 0
    if not any("G" in rule for rule in grid):   # if no G's in the grid, return 0
        return 0
    for i in range(1, len(grid)-1):         # Elk cel langs die niet aan de rand zit
        for j in range(1, len(grid[0])-1):
            maximum = 0
            grid_new = grid.copy()
            if grid[i][j] == "G":
                area = 1            # Een g, dus area altijd minimaal 1
                grid_new[i] = grid_new[i][:j] + "B" + grid_new[i][j + 1:]   # De cel zelf van G naar B
                # Bepaal voor deze cel de grootte van de plus
                print(i, "-", j)
                # Bepaal hoe groot de plus maximaal kan zijn (theoretische plusgrootte):
                min_abov_undr = min((len(grid)-int(i)-1), i)
                min_left_right = min(j, (len(grid[0])-int(j))-1)
                maximum = min(min_abov_undr, min_left_right)        # Plus kan maximaal [maximum] groot zijn.
                plusgrootte = 0
                for max in range(1, maximum+1):     # Hoe groot is de plus daadwerkelijk:
                    if grid[i-max][j] == "G" and grid[i+max][j] == "G" and grid[i][j-max] == "G" and grid[i][j+max] == "G":
                        print("Rondom allemaal G's")
                        # De G's veranderen in B's:
                        grid_new[i-max] = grid_new[i-max][:j] + "B" + grid_new[i-max][j+1:]    # cel boven bewuste cel
                        grid_new[i+max] = grid_new[i+max][:j] + "B" + grid_new[i+max][j+1:]    # cel onder bewuste cel
                        grid_new[i] = grid_new[i][:j - max] + "B" + grid_new[i][j - max + 1:]  # cel links
                        grid_new[i] = grid_new[i][:j + max] + "B" + grid_new[i][j + max + 1:]  # cel rechts
                        plusgrootte += 1
                        area = (4 * plusgrootte) + 1
                    else:
                        break                     # Stoppen want maximale plus bereikt
                print("Bij deze plus is de area: {}".format(area))
                print("gr_n: {}".format(grid_new))

                # Met het nieuwe grid waar de plus op de cel gemarkeerd is als B's, opnieuw de grootste plus zoeken:
                for k in range(1, len(grid_new) - 1):  # Elk cel langs die niet aan de rand zit
                    for l in range(1, len(grid_new[0]) - 1):
                        if grid_new[k][l] == "G":
                            print(k, "-", l)
                            area_new = 1
                            # Bepaal hoe groot deze plus maximaal kan zijn (theoretische plusgrootte):
                            min_abov_undr = min((len(grid) - int(k) - 1), k)
                            min_left_right = min(l, (len(grid[0]) - int(l)) - 1)
                            maximum = min(min_abov_undr, min_left_right)  # Plus kan maximaal [maximum] groot zijn.
                            print("Max.grootte is: {}".format(maximum))
                            plusgrootte = 0
                            for max in range(1, maximum + 1):  # Hoe groot is deze plus daadwerkelijk:
                                if grid_new[k - max][l] == "G" and grid_new[k + max][l] == "G" and grid_new[k][l - max] == "G" and \
                                        grid_new[k][l + max] == "G":
                                    print("Rondom allemaal G's")
                                    plusgrootte += 1
                                    area_new = (4 * plusgrootte) + 1
                                else:
                                    break
                            # Bereken area eerste keer tweede area
                            if area * area_new > max_area:
                                max_area = area * area_new

                print("-----------------------------")
    print("max_area: {}".format(max_area))

# TODO: Als er alleen G's in de randcellen zitten: check of er 2 G's in zitten. Return is dan 1



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

2 2
BG
BB

"""