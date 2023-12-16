

total=0
grid=[] # store tile(x,y) -> grid[y][x]

# Opening file
file = open('day16.txt', 'r')
for line in file:
    grid.append(line.strip())
file.close()

print('\n'.join(grid))

def straight_beam(beam):
    """ return 1 beam with same direction"""
    if beam[2]=='>':
        return (beam[0]+1, beam[1], beam[2])
    elif beam[2]=='<':
        return (beam[0]-1, beam[1], beam[2])
    elif beam[2]=='^':
        return (beam[0], beam[1]-1, beam[2])
    elif beam[2]=='v':
        return (beam[0], beam[1]+1, beam[2])

def deflect_beam(beam, tile):
    """ return 1 beam with direction bent 90 degrees"""
    dir=beam[2]
    if dir=='>' and tile=='/': # up
        return (beam[0], beam[1]-1, '^')
    if dir=='>' and tile=='\\': # down
        return (beam[0], beam[1]+1, 'v')
    if dir=='<' and tile=='/': # down
        return (beam[0], beam[1]+1, 'v')
    if dir=='<' and tile=='\\': # up
        return (beam[0], beam[1]-1, '^')
    
    if dir=='v' and tile=='/': # left
        return (beam[0]-1, beam[1], '<')
    if dir=='v' and tile=='\\': # right
        return (beam[0]+1, beam[1], '>')
    if dir=='^' and tile=='/': # right
        return (beam[0]+1, beam[1], '>')
    if dir=='^' and tile=='\\': # left
        return (beam[0]-1, beam[1], '<')

def split_beam(beam, tile):
    """ return 2 split beams or 1 passthrough"""
    dir=beam[2]
    if dir in '><' and tile=='|':
        return (beam[0], beam[1]-1, '^'), (beam[0], beam[1]+1, 'v')
    if dir in 'v^' and tile=='-':
        return (beam[0]-1, beam[1], '<'), (beam[0]+1, beam[1], '>')
    return straight_beam(beam), None

def on_grid(beam, grid):
    """ check if position is out of bounds """
    if beam is None: return False
    x=beam[0]
    y=beam[1]
    if x<0: return False
    if y<0: return False
    if x>=len(grid[0]): return False
    if y>=len(grid): return False
    return True

def trace_beam(start):
    """ expands the given start beam, returns number of covered grid cells """
    openlist=[] # store x,y,dir
    openlist.append( start )

    closedlist=[]

    while len(openlist)>0 :
        beam=openlist.pop()

        try:
            tile=grid[beam[1]][beam[0]]
        except IndexError: 
            continue # dismiss beam outside grid

        next=None
        next2=None
        if tile=='.':
            next=straight_beam(beam)
        elif tile in '/\\':
            next=deflect_beam(beam, tile)
        elif tile in '|-':
            next, next2=split_beam(beam, tile)
        
        if on_grid(next, grid) and next not in closedlist: 
            openlist.append(next)
        if on_grid(next2, grid) and next2 not in closedlist: 
            openlist.append(next2)

        if beam not in closedlist:
            closedlist.append(beam)

    # msg="open: {} closed: {}"
    # print(msg.format(len(openlist), len(closedlist)))

    return len(set(map(lambda x: (x[0],x[1]), closedlist)))


# main loop
max=len(grid)-1
for i in range(len(grid)):
    print(i)
    msg="energized: {} total: {}"

    energized=trace_beam( (i,0,'v') )
    if energized>total: total=energized
    print(msg.format(energized, total))

    energized=trace_beam( (i,max,'^') )
    if energized>total: total=energized
    print(msg.format(energized, total))

    energized=trace_beam( (0,i,'>') )
    if energized>total: total=energized
    print(msg.format(energized, total))

    energized=trace_beam( (max,i,'<') )
    if energized>total: total=energized
    print(msg.format(energized, total))

print(total)