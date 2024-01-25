with open("day21.txt", "r") as file:
    grid = tuple(file.read().splitlines())

print("grid size: {} ({} x {})".format(len(grid)*len(grid[0]), len(grid[0]), len(grid)))

# locate start 'S'
for y, row in enumerate(grid):
    x=row.find('S')
    if x>=0:
        start=(x,y)
        break

# connected neighbors on grid:
# starting position (S), garden plots (.), and rocks (#)
def expand(item):
    " provides successor garden plots if on grid "
    successors=[]
    pos=item
    for dir in "nswe":
        newpos=(pos[0]+neighbors[dir][0], pos[1]+neighbors[dir][1])
        if newpos[0]<0 or newpos[0]>=len(grid[0]) or newpos[1]<0 or newpos[1]>=len(grid): 
            continue
        g1=grid[pos[1]][pos[0]]
        g2=grid[newpos[1]][newpos[0]]

        if g2!='#':
            successors.append(newpos)

    return successors


neighbors={'n':(0,-1), 's':(0,1), 'w':(-1,0), 'e':(1,0)}
openlist=set()
openlist.add(start)

step = 0
while len(openlist)>0:
    step += 1
    # expand all items
    newlist=set()
    for item in openlist:
        successors=expand(item)
        for n in successors:
            newlist.add(n)
    openlist=newlist
    print(len(openlist))

    # test position match
    if step==64:
        break

print(step)

