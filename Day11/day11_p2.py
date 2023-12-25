# try making the expansion edge weights

import sys
from tqdm import tqdm

def printMatrix(matrix):
    for row in matrix:
        print(''.join(row))
    print()


def expand_universe(matrix):
    empty_rows = []
    for i in range(len(matrix)):
        if '#' not in matrix[i]:
            empty_rows.append(i)
    
    for i in range(len(empty_rows)):
        matrix[empty_rows[i]:empty_rows[i]] = ['.' * len(matrix[0])]
        empty_rows = list(map(lambda x: x + 1, empty_rows))
        
    return matrix


def calculate_distance(node1, node2):
    return abs(node1[0] - node2[0]) + abs(node1[1] - node2[1])


def get_positions(universe):
    galaxy_positions = {}
    for i in range(len(universe)):
        for j in range(len(universe[i])):
            if universe[i][j] == '#':
                galaxy_positions[len(galaxy_positions)] = (i,j)
    return galaxy_positions
    

def run(universe):
    original_positions = get_positions(universe)
    
    original_matrix = [[-1]*len(original_positions)]*len(original_positions)
    
    # for i in range(len(original_positions)):
    #     for j in range(len(original_positions)):
    #         dist = calculate_distance(original_positions[i], original_positions[j])
    #         print(i,j,dist)

    #         if original_matrix[i][j] == -1:
    #             original_matrix[i][j] = dist
                
    for j in range(len(original_positions)):
        dist = calculate_distance(original_positions[1], original_positions[j])
        if original_matrix[1][j] == -1:
            original_matrix[1][j] = dist
           
    for n in original_matrix:
        print(n)
    print()
    
    # expand the universe
    universe = expand_universe(universe)

    universe = [list(col) for col in zip(*universe)]
    universe = expand_universe(universe)
    universe = [list(col) for col in zip(*universe)]
        
    # find galaxy positions
    galaxy_positions = get_positions(universe)    

    ans = 0
    for i in range(len(galaxy_positions)):
        for j in range(len(galaxy_positions)):
            ans += calculate_distance(galaxy_positions[i], galaxy_positions[j])
    
    print(original_positions)
    print(galaxy_positions)
    print(int(ans/2))

    
universe = open(sys.argv[-1], 'r').read().splitlines()

run(universe)
        