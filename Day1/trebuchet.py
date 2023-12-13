import re

def part1():
    f = open("in.txt", "r")
    
    ans = 0
    for line in f:
        digits = [x for x in line if x.isdigit()]
        val = digits[0] + digits[-1]
        ans = ans + int(val)
        
    print(ans)
    
def part2():
    f = open("in.txt", "r")
    pattern = "(one|two|three|four|five|six|seven|eight|nine|[0-9])"
    dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    ans = 0
    for line in f:
        line = re.sub("twone", "21", line)
        line = re.sub("eighthree", "83", line)
        line = re.sub("sevenine", "79", line)
        line = re.sub("eightwo", "82", line)
        line = re.sub("oneight", "18", line)
        
        match = re.findall(pattern, line)
        print(match)
        first = match[0] if match[0].isdigit() else dict[match[0]]
        last = match[len(match)-1] if match[len(match)-1].isdigit() else dict[match[len(match)-1]]
        
        val = str(first) + str(last)
        ans += int(val)
        
    print(ans)
    
part1()
part2()