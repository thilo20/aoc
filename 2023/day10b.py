# day 10 part 2:
# - the loop is a "simple polygon" (no holes, no self intersections)
# - tiles that are enclosed by the loop == polygon area
# - collect loop coordinates
# - convert to polygon representation
# - calculate area
# area calculation dismissed.. too complicated as "squeezing between pipes is also allowed" (but area would be >0)
# instead, we can check if a grid tile is inside the polygon (and count them)

with open("day10.txt", "r") as file:
    grid = tuple(file.read().splitlines())

# locate start 'S'
for y, row in enumerate(grid):
    x=row.find('S')
    if x>=0:
        start=(x,y)
        break

# connected neighbors on grid:
    # | is a vertical pipe connecting north and south.
    # - is a horizontal pipe connecting east and west.
    # L is a 90-degree bend connecting north and east.
    # J is a 90-degree bend connecting north and west.
    # 7 is a 90-degree bend connecting south and west.
    # F is a 90-degree bend connecting south and east.
    # . is ground; there is no pipe in this tile.
    # S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
def connected(item):
    " provides successor pipe if on grid and matching connection "
    pos, dir=item
    newpos=(pos[0]+neighbors[dir][0], pos[1]+neighbors[dir][1])
    if newpos[0]<0 or newpos[0]>=len(grid[0]) or newpos[1]<0 or newpos[1]>=len(grid): 
        return None
    g1=grid[pos[1]][pos[0]]
    g2=grid[newpos[1]][newpos[0]]

    newdir=None
    if dir=='n' and g2=='|': newdir='n'
    elif dir=='n' and g2=='7': newdir='w'
    elif dir=='n' and g2=='F': newdir='e'
    elif dir=='s' and g2=='|': newdir='s'
    elif dir=='s' and g2=='J': newdir='w'
    elif dir=='s' and g2=='L': newdir='e'
    elif dir=='w' and g2=='-': newdir='w'
    elif dir=='w' and g2=='L': newdir='n'
    elif dir=='w' and g2=='F': newdir='s'
    elif dir=='e' and g2=='-': newdir='e'
    elif dir=='e' and g2=='J': newdir='n'
    elif dir=='e' and g2=='7': newdir='s'

    if newdir is None:
        return None
    return (newpos, newdir)


neighbors={'n':(0,-1), 's':(0,1), 'w':(-1,0), 'e':(1,0)}
openlist=[*zip([start]*4, neighbors)]

# - collect loop coordinates
loop=[start]

step = 0
while len(openlist)>0:
    step += 1
    # expand all items
    newlist=[]
    for item in openlist:
        neighbor=connected(item)
        if neighbor is not None:                   
            newlist.append(neighbor)
    openlist=newlist
    [loop.append(item[0]) for item in newlist]

    # test position match
    if len(set(map(lambda item: item[0], openlist)))<2:
        break

print(openlist)
print(step)
print("loop length: ", len(loop))
print("grid size: {} ({} x {})".format(len(grid)*len(grid[0]), len(grid[0]), len(grid)))
print("max.points in/outside: ", len(grid)*len(grid[0])-len(loop))

# - convert to polygon representation
from shapely.geometry import Polygon, Point
coords=[loop[0], *loop[1::2], *loop[-1:0:-2], loop[0]]
pgon = Polygon(coords)
print(pgon.area, pgon.is_simple)

# - calculate area
count = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if (x, y) not in coords and pgon.contains(Point(x, y)):
        # if pgon.contains(Point(x, y)) and (x, y) not in coords:
        # if pgon.contains(Point(x, y)): # same result, so points on polygon border don't count as 'contained'
            count += 1

print(count)

# timings
# python3 day10b.py  17.42s user 0.39s system 105% cpu 16.871 total
# python3 day10b.py  58.52s user 0.44s system 101% cpu 58.043 total (flipped conditions, line 96)
