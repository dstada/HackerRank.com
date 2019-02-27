

def cavityMap(grid):
    print(grid)



if __name__ == '__main__':
    n = int(input())
    grid = []
    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)
    result = cavityMap(grid)
    print(result)