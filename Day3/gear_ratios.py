import sys
import re
import math

def part1():
    file = open(sys.argv[-1], 'r').read().split('\n')
    
    numbers = []
    symbols = []
    for line in file:
        number = []
        symbol = []
        for match in re.finditer(r"\d+", line):
            number.append(match)
        for match in re.finditer(r"[^0-9.]", line):
            symbol.append(match)
        numbers.append(number)
        symbols.append(symbol)
    
    matches = set()
    for i in range(len(symbols)):
        for s in symbols[i]:
            s1, e1 = s.span()
            for nline in numbers[i-1:i+2]:
                for n in nline:
                    s2, e2 = n.span()
                    if s1 >= s2-1 and e1 <= e2+1:
                        matches.add(n)

    print(sum([int(i.group()) for i in matches]))
    
def part2():
    file = open(sys.argv[-1], 'r').read().split('\n')
    
    numbers = []
    symbols = []
    for line in file:
        number = []
        symbol = []
        for match in re.finditer(r"\d+", line):
            number.append(match)
        for match in re.finditer(r"[*]", line):
            symbol.append(match)
        numbers.append(number)
        symbols.append(symbol)
        
    ans = 0
    for i in range(len(symbols)):
        for s in symbols[i]:
            part_numbers = set()
            s1, e1 = s.span()
            print("S: ",s1,e1,s.group())
            for nline in numbers[i-1:i+2]:
                for n in nline:
                    s2, e2 = n.span()
                    if s1 >= s2-1 and e1 <= e2+1:
                        print("N: ",s2,e2,n.group())
                        part_numbers.add(n)
            if len(part_numbers) == 2:
                ans += (math.prod([int(i.group()) for i in part_numbers]))

    print(ans)
    
# part1()
part2()