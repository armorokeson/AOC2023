import sys
import re

def calculate_distance(time, hold):
    return (time - hold) * hold

def find_win_strats(race):
    time = race[0]
    record = race[1]
    win_strats = 0
    
    for i in range(2,time):
        if calculate_distance(time, i) > record:
            win_strats += 1
    
    return win_strats

def part1():
    file = open(sys.argv[-1], 'r')
    times = list(map(int, re.findall(r'\d+', file.readline())))
    distances = list(map(int, re.findall(r'\d+', file.readline())))
    races = zip(times, distances)

    margin_error = 1
    for race in races:
        margin_error *= find_win_strats(race)
        
    print(margin_error)
    
def part2():
    file = open(sys.argv[-1], 'r')
    times = re.findall(r'\d+', file.readline())
    distances = re.findall(r'\d+', file.readline())
    
    time = int(''.join(times))
    distance = int(''.join(distances))
    
    print(find_win_strats((time,distance)))

# part1()
part2()
