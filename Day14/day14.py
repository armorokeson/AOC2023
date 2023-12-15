import sys
from tqdm import tqdm

file = open(sys.argv[-1], 'r').read().splitlines()

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
            
print()
for n in platform:
    print(''.join(n))
                            
platform = [list(col) for col in list(zip(*platform))]

print()
for n in platform:
    print(''.join(n))

load = 0
row_load = 10
for row in platform:
    load += row_load * row.count('O')
    row_load -= 1
    
print(load)
