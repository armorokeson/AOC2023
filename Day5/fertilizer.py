import sys
import re
import threading
import time
from tqdm import tqdm

def mapper(s, m):
    for n in m:
        if s >= n[1] and s <= n[1] + n[2]:
            return (s - n[1]) + n[0]

    return s

def getLocations(seeds, maps):
    curr_smallest = sys.maxsize
    for i in tqdm(range(len(seeds))):
        location = seeds[i]
        for m in maps:
            # make them all ints so I dont have to cast
            m = list(map(int, re.findall(r'\d+', m)))
            
            # group each map
            n = []
            for i in range(0, len(m), 3):
                n.append(m[i:i+3])
            
            location = mapper(location, n)
            
        if seeds[i] == seeds[0]:
            curr_smallest = location
            
        if location < curr_smallest:
            curr_smallest = location
            
    return curr_smallest

def part1():
    file = open(sys.argv[-1], 'r')
    seeds = list(map(int, re.findall(r'\d+', file.readline())))
    maps = file.read().split('\n\n')
    
    print(getLocations(seeds, maps))
    
def part2():
    file = open(sys.argv[-1], 'r')
    seed_list = list(map(int, re.findall(r'\d+', file.readline())))
    maps = file.read().split('\n\n')
    
    seed_ranges = []
    for i in range(0,len(seed_list)-1,2):
        seed_ranges.append((seed_list[i], seed_list[i+1]))
        
    print(seed_ranges)
        
    # seeds = []
    # for r in seed_ranges:
    #     seeds += range(r[0], r[0] + r[1])
        
    # print(len(seeds))
    
    # this is only the first range. there are like 18. this one has 71,155,519 values
    # 1,680,883,088
    seeds = range(seed_ranges[0][0], seed_ranges[0][0] + seed_ranges[0][1])
        
    print(getLocations(seeds, maps))
    
# part1()

start = time.time()
part2()
end = time.time()
print(round(end-start, 2), "s")