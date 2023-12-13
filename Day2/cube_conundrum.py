import sys

def part1():
    file = open(sys.argv[-1], 'r')
    total_red = 12
    total_green = 13
    total_blue = 14
    
    ans = 0
    for game in file:
        split1 = game.split(':')
        game_id = int(split1[0][5:])
        
        possible = True
        draws = split1[1].split(';')
        for draw in draws:
            cubes = draw.split(',')
            red = 0
            green = 0
            blue = 0
            for cube in cubes:
                if 'red' in cube:
                    red = int(cube[:-4])
                elif 'green' in cube:
                    green = int(cube[:-6])
                elif 'blue' in cube:
                    blue = int(cube[:-5])
                    
            if red > total_red or blue > total_blue or green > total_green:
                possible = False
                break
            
        if possible:
            ans += game_id
    
    print(ans)
    
def part2():
    file = open(sys.argv[-1], 'r')
    
    ans = 0
    for game in file:
        split1 = game.split(':')
        
        draws = split1[1].split(';')
        red = []
        green = []
        blue = []
        for draw in draws:
            cubes = draw.split(',')
            for cube in cubes:
                if 'red' in cube:
                    red.append(int(cube[:-4]))
                elif 'green' in cube:
                    green.append(int(cube[:-6]))
                elif 'blue' in cube:
                    blue.append(int(cube[:-5]))
        
        ans += (max(red) * max(green) * max(blue))
        
    print(ans)
    
part1()
part2()