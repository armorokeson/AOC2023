import sys
from tqdm import tqdm

MULTIPLIER = 2

def printMatrix(matrix):
    for row in matrix:
        print(''.join(row))
    print()

def expand_universe(matrix):
    empty_rows = []
    for i in range(len(matrix)):
        if '#' not in matrix[i]:
            empty_rows.append(i)
    
    for i in tqdm(range(len(empty_rows))):
        matrix[empty_rows[i]:empty_rows[i]] = ['.' * len(matrix[0])] * MULTIPLIER
        empty_rows = list(map(lambda x: x + MULTIPLIER, empty_rows))
        
    return matrix


def calculate_distance(node1, node2):
    return abs(node1[0] - node2[0]) + abs(node1[1] - node2[1])
    

def run(universe):
    # expand the universe
    # universe = expand_universe(universe)

    # universe = [list(col) for col in zip(*universe)]
    # universe = expand_universe(universe)
    # print("\n\t---Expansion Complete---\n")
    # universe = [list(col) for col in tqdm(zip(*universe))]
    # printMatrix(universe)
    
    empty_rows = []
    for i in range(len(universe)):
        if '#' not in universe[i]:
            empty_rows.append(i)
            
    empty_cols = []
    universe_columns = [list(col) for col in zip(*universe)]
    for i in range(len(universe_columns)):
        if '#' not in universe_columns[i]:
            empty_cols.append(i)
        
    # find galaxy positions
    galaxy_positions = {}
    for i in tqdm(range(len(universe))):
        for j in range(len(universe[i])):
            if universe[i][j] == '#':
                galaxy_positions[len(galaxy_positions)] = (i,j)
                
    # print(galaxy_positions)
    
    matrix = [[-1] * len(galaxy_positions)]*len(galaxy_positions)

    ans = 0
    for i in tqdm(range(len(galaxy_positions))):
        for j in range(len(galaxy_positions)):
            g1 = galaxy_positions[i]
            g2 = galaxy_positions[j]
            
            for n in empty_rows:
                if g1[1] <= n and g2[1] >= n:
                    g2 = (g2[0], g2[1] + 1)
                    
            for n in empty_cols:
                if g1[0] <= n and g2[0] >= n:
                    g2 = (g2[0] + 1, g2[1])
                    
            # print(g1, g2)
            
            if matrix[i][j] == -1:
                dist = calculate_distance(g1, g2)
                matrix[i][j] = dist
        for n in matrix:
            print(n)
        print()
    
    print(galaxy_positions)
    for n in matrix:
        print(n)
    print()
    print(list(map(sum, matrix)))

    
universe = open(sys.argv[-1], 'r').read().splitlines()

run(universe)
        