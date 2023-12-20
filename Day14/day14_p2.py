import sys
from tqdm import tqdm


# perform one tilt
def perform_tilt(platform):
    # move round rocks as far as they can go
    for i in range(len(platform)):
        empty_space = 0
        for j in range(len(platform[i])):
            if platform[i][j] == '.':
                empty_space += 1 
            elif platform[i][j] == 'O' and empty_space > 0:
                # move the rock as far as it can go
                platform[i][j-empty_space] = 'O'
                platform[i][j] = '.'
            else:
                empty_space = 0
    return platform


# calcuate the load of the platform
def calc_load(platform):
    load = 0
    row_load = len(platform)
    for row in platform:
        load += row_load * row.count('O')
        row_load -= 1
    return load


plat = open(sys.argv[-1], 'r').read().splitlines()

for i in tqdm(range(1000)):
    # tilt north
    plat = perform_tilt([list(col) for col in zip(*plat)])
    plat = [list(col) for col in zip(*plat)]

    # tilt west
    plat = perform_tilt(plat)

    # tilt south
    plat = perform_tilt([list(reversed(list(col))) for col in zip(*plat)])
    plat = [list(reversed(row)) for row in plat]
    plat = [list(col) for col in zip(*plat)]

    # tilt east
    plat = perform_tilt([list(reversed(row)) for row in plat])
    plat = [list(reversed(row)) for row in plat]
    
print(calc_load(plat))


# north: list of columns
# south: list of columns (reversed)
# east:  list of rows (reversed)
# west:  list of rows 
