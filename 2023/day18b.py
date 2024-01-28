import re

total=0

plan=[] # (x,y) digged out
points=[] # (x,y) polygon points
start=(0,0)
pos=start
border=0 # length of border (area boundary)

dir={'3': (0,-1), '1': (0,1), '2': (-1,0), '0': (1,0)}

# Opening file
file = open('day18.txt', 'r')
for line in file:
    command=re.findall("#(.{5})(.)", line)
    d=dir[command[0][1]]
    steps=int(command[0][0], 16)
    border+=steps
    pos=(pos[0]+d[0]*steps, pos[1]+d[1]*steps) # tuple math sucks, python ;)
    points.append(pos)
file.close()

# https://github.com/derailed-dash/Advent-of-Code/blob/master/src/AoC_2023/Dazbo's_Advent_of_Code_2023.ipynb
def shoelace_area(polygon: list[tuple[int,int]]) -> int:
    """ calc area with triangle formula, see https://en.wikipedia.org/wiki/Shoelace_formula """
    total = 0
    for i, (x,y) in enumerate(polygon):
        next_index = (i+1) % len(polygon)
        prev_index = i-1
        total += x*(polygon[next_index][1] - polygon[prev_index][1])
        
    return abs(total) // 2


print("area border:   ", border)
print("shoelace area: ", shoelace_area(points))

total=shoelace_area(points)+border//2+1
print(total)
