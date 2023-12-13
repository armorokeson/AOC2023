import sys

top = '|7F'         # valid if on top
bottom = '|LJ'      # valid if on bottom
left = '-LF'        # valid if on left side
right = '-7J'       # valid if on right side

def find_start_pos(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'S':
                return (i,j)
            

def map_to_next_dir(position_from_last, pipe):
    if position_from_last == 1:
        if pipe == '|': return 1
        if pipe == '7': return 2 
        if pipe == 'F': return 3
    if position_from_last == 2:
        if pipe == 'L': return 2
        if pipe == '-': return 3
        if pipe == 'F': return 4
    if position_from_last == 3:
        if pipe == 'J': return 1
        if pipe == '-': return 3
        if pipe == '7': return 4
    if position_from_last == 4:
        if pipe == 'J': return 2
        if pipe == 'L': return 3
        if pipe == '|': return 4

            
def solve(maze, s1r, s1c, s2r, s2c, s1_from_start, s2_from_start):
    curr_pipe1 = None
    curr_pipe2 = None 

    while True:
        None


def part1():
    maze = open(sys.argv[-1], 'r').read().splitlines()
    
    # adding some padding so dont have to worry about out of bounds checks
    maze.append('.'*(len(maze[0])))
    maze.insert(0, '.'*(len(maze[0])))
    for i in range(len(maze)):
        maze[i] = '.' + maze[i] + '.'
        
    for line in maze:
        print(line)
    
    # get the position of our starting location
    (sr,sc) = find_start_pos(maze)

    # find where the loop starts on either end of s
    if maze[sr-1][sc] in top:
        side1 = (sr-1, sc, 1)
    else:
        side1 = (sr, sc+1, 3)
    
    if maze[sr+1][sc] in bottom:
        side2 = (sr+1, sc, 4)
    else:
        side2 = (sr, sc-1, 2)
    
    
    
part1()

#   1
# 2 S 3
#   4
