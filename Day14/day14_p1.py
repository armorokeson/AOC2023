import sys
from tqdm import tqdm

file = open(sys.argv[-1], 'r').read().splitlines()

# rotate matrix
file = list(zip(*file))
platform = [list(col) for col in file]

# OO.O.O..##
# ...OO....O
# .O...#O..O
# .O.#......
# .#.O......
# #.#..O#.##
# ..#...O.#.
# ....O#.O#.
# ....#.....
# .#.O.#O...

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
                            
# rotate it back                           
platform = [list(col) for col in list(zip(*platform))]

load = 0
row_load = len(platform)
for row in platform:
    load += row_load * row.count('O')
    row_load -= 1
    
print(load)
