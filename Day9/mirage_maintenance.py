import sys
import re

def solve(line, p2):
    diffs = []
    for i in range(len(line)-1):
        diffs.append(line[i+1] - line[i])

    ans = 0
    if not all(n == 0 for n in diffs):
        if p2:
            ans += diffs[0] - solve(diffs, p2)
        else:
            ans += solve(diffs, p2) + diffs[-1]
            
    diffs.insert(0,ans)
    print(diffs)
    return ans

def part1():
    file = open(sys.argv[-1], 'r').read().splitlines()
    report = []
    for line in file:
        report.append(list(map(int, re.findall(r'-?\d+', line))))

    for line in report:
        next_val = solve(line, False) + line[-1]
        line.append(next_val)
        print(line)

    ans = 0
    for line in report:
        ans += line[-1]
    print(ans)

def part2():
    file = open(sys.argv[-1], 'r').read().splitlines()
    report = []
    for line in file:
        report.append(list(map(int, re.findall(r'-?\d+', line))))

    for line in report:
        next_val =  line[0] - solve(line, True)
        line.insert(0,next_val)
        print(line)

    ans = 0
    for line in report:
        ans += line[0]
    print(ans)

# part1()
part2()
