import sys
import re

def check_record(springs, sizes):
    springs = ''.join(springs)
    print(springs)
    groups = list(map(len, re.findall(r'[#]+', springs)))
    if groups == sizes:
        return 1
    return 0

def solve(springs, sizes):
    solutions = 0

    for i in range(len(springs)):
        if springs[i] != '?':
            continue
        springs[i] = '#'
        solutions += solve(springs, sizes)
        springs[i] = '.'
        return solutions + solve(springs, sizes)

    return check_record(springs, sizes)

def p1():
    records = open(sys.argv[-1], 'r').readlines()
    
    ans = 0
    for record in records:
        (springs,sizes) = re.split(' ', record)
        sizes = list(map(int,re.findall(r'\d+', sizes)))
        ans += solve(list(springs), sizes)
    
    print(ans)
        
p1()