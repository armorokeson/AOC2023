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
            
            
def solve(maze, start1, start2):
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
    side1 = (sr-1,sc) if maze[sr-1][sc] in top else (sr,sc+1)
    side2 = (sr+1,sc) if maze[sr+1][sc] in bottom else (sr+1,sc)  
    
    
part1()


#   1
# 2 S 3
#   4

# 1,7 = - or F 
# 1,| = | or 7 or F
# 1,F = - or 7 
# 2,F = - or 7
# 2,L = - or F
# 2,- = F or L or J 