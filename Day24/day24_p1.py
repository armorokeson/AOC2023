import sys
import re
import math

lower_bound = 200000000000000
upper_bound = 400000000000000

# lower_bound = 7
# upper_bound = 27

def solve(hailstoneA, hailstoneB):
    (p1,v1) = hailstoneA.split('@')
    (p2,v2) = hailstoneB.split('@')
    
    p1 = list(map(float,re.findall(r'-?\d+', p1)))
    v1 = list(map(float,re.findall(r'-?\d+', v1)))
    
    p2 = list(map(float,re.findall(r'-?\d+', p2)))
    v2 = list(map(float,re.findall(r'-?\d+', v2)))
     
    cross_product = v1[0] * v2[1] - v1[1] * v2[0]
    
    if cross_product == 0:
        print("Hailstones are parallel")
        return 0
        
    t1 = ((p2[0] - p1[0]) * v2[1] - (p2[1] - p1[1]) * v2[0]) / cross_product
    t2 = ((p2[0] - p1[0]) * v1[1] - (p2[1] - p1[1]) * v1[0]) / cross_product
    if t1 < 0 and t2 < 0:
        print("Hailstones' paths crossed in the past for both hailstones")
        return 0
    elif t1 < 0:
        print("Hailstones' paths crossed in the past for hailstone A")
        return 0
    elif t2 < 0:
        print("Hailstones' paths crossed in the past for hailstone B")
        return 0
    else:
        (x,y) = (p1[0] + t1 * v1[0], p1[1] + t1 * v1[1])
        
        if lower_bound <= x <= upper_bound and lower_bound <= y <= upper_bound:
            print(f"Hailstones' paths will cross INSIDE the test area (at x={x}, y={y}, t={t1})")
            return 1
        else:
            print(f"Hailstones' paths will cross OUTSIDE the test area (at x={x}, y={y}, t={t1})")
            return 0
    
hailstones = open(sys.argv[-1], 'r').read().splitlines()

ans = 0
for i,a in enumerate(hailstones):
    for b in hailstones[i+1:]:
        print("Hailstone A: ", a)
        print("Hailstone B: ", b)
        res = solve(a, b)
        ans += res
        print()
print(f"{ans} hailstones intersect inside the test area")
