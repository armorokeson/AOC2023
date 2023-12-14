import sys

#   1
# 2 S 3
#   4

top = '|7F'         # valid if on top
bottom = '|LJ'      # valid if on bottom
left = '-LF'        # valid if on left side
right = '-7J'       # valid if on right side

def find_first_second_pipe(maze, start):
    (sr,sc) = start
    if maze[sr-1][sc] in top:
        side1 = (sr-1, sc, 1)
        if maze[sr+1][sc] in bottom:
            side2 = (sr+1, sc, 4)
        elif maze[sr][sc+1] in right:
            side2 = (sr, sc+1, 3)
        elif maze[sr][sc-1] in left:
            side2 = (sr, sc-1, 2)
    elif maze[sr+1][sc] in bottom:
        side1 = (sr+1, sc, 4)
        if maze[sr-1][sc] in top:
            side2 = (sr-1, sc, 1)
        elif maze[sr][sc+1] in right:
            side2 = (sr, sc+1, 3)
        elif maze[sr][sc-1] in left:
            side2 = (sr, sc-1, 2)
    elif maze[sr][sc+1] in right:
        side1 = (sr, sc+1, 3)
        if maze[sr-1][sc] in top:
            side2 = (sr-1, sc, 1)
        elif maze[sr+1][sc] in bottom:
            side2 = (sr+1, sc, 4)
        elif maze[sr][sc-1] in left:
            side2 = (sr, sc-1, 2)
    elif maze[sr][sc-1] in left:
        side1 = (sr, sc-1, 2)
        if maze[sr-1][sc] in top:
            side2 = (sr-1, sc, 1)
        elif maze[sr+1][sc] in bottom:
            side2 = (sr+1, sc, 4)
        elif maze[sr][sc+1] in right:
            side2 = (sr, sc+1, 3)
            
    return side1,side2

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
        if pipe == 'L': return 1
        if pipe == '-': return 2
        if pipe == 'F': return 4
    if position_from_last == 3:
        if pipe == 'J': return 1
        if pipe == '-': return 3
        if pipe == '7': return 4
    if position_from_last == 4:
        if pipe == 'J': return 2
        if pipe == 'L': return 3
        if pipe == '|': return 4
    return(-1)

            
def solve(maze, s1r, s1c, s2r, s2c, s1_from_start, s2_from_start, start):
    steps = 0
    while True:
        steps += 1

        if s1r == s2r and s1c == s2c:
            return steps
        
        next_pipe = map_to_next_dir(s1_from_start, maze[s1r][s1c])
        s1_from_start = next_pipe
        
        if next_pipe == 1:   s1r -= 1
        elif next_pipe == 2: s1c -= 1
        elif next_pipe == 3: s1c += 1
        elif next_pipe == 4: s1r += 1
        
        next_pipe = map_to_next_dir(s2_from_start, maze[s2r][s2c])
        s2_from_start = next_pipe
        
        if next_pipe == 1:   s2r -= 1
        elif next_pipe == 2: s2c -= 1
        elif next_pipe == 3: s2c += 1
        elif next_pipe == 4: s2r += 1


def part1():
    maze = open(sys.argv[-1], 'r').read().splitlines()
    
    # adding some padding so dont have to worry about out of bounds checks
    maze.append('.'*(len(maze[0])))
    maze.insert(0, '.'*(len(maze[0])))
    for i in range(len(maze)):
        maze[i] = '.' + maze[i] + '.'
    
    # get the position of our starting location
    (sr,sc) = start = find_start_pos(maze)

    # find where the loop starts on either end of s
    side1,side2 = find_first_second_pipe(maze, start)
    
    print(solve(maze, side1[0], side1[1], side2[0], side2[1], side1[2], side2[2], start))
       
part1()
