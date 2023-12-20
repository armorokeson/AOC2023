import sys

def expand_universe(matrix):
    empty_rows = []
    for i in range(len(matrix)):
        if '#' not in matrix[i]:
            empty_rows.append(i)
    
    for i in range(len(empty_rows)):
        matrix.insert(empty_rows[i] + 1, '.' * len(matrix[0]))
        
    return matrix


def calculate_distance(node1, node2):
    return abs(node1[0] - node2[0]) + abs(node1[1] - node2[1])
    

universe = open(sys.argv[-1], 'r').read().splitlines()

# expand the universe
universe = expand_universe(universe)
universe = expand_universe([list(cols) for cols in zip(*universe)])
universe = [list(cols) for cols in zip(*universe)]
        
for row in universe:
    print(''.join(row))
    
# find galaxy positions
galaxy_positions = {}
for i in range(len(universe)):
    for j in range(len(universe[i])):
        if universe[i][j] == '#':
            galaxy_positions[len(galaxy_positions) + 1] = (i,j)
            
print(galaxy_positions)

ans = 0
for i in range(1, len(galaxy_positions)+1):
    for j in range(1, len(galaxy_positions)+1):
        ans += calculate_distance(galaxy_positions[i], galaxy_positions[j])
        
print((ans/2)-len(universe))
        