

total=0
grid=[] # store tile(x,y) -> grid[y][x]

# Opening file
file = open('day23-test.txt', 'r')
for line in file:
    grid.append(line.strip())
file.close()

print('\n'.join(grid))


def move_on(hiker, grid):
    """ return 0..3 hikers moved one step forward """
    res=[]
    pos=(hiker[0],hiker[1])
    dir=hiker[2]
    field=grid[hiker[1]][hiker[0]]

    # been here before?
    if len(hiker)>3 and pos in hiker[3]:
        return res
    
    # on slope
    # if field == '>':
    #     res.append((hiker[0]+1, hiker[1], '>'))
    # elif field == '<':
    #     res.append((hiker[0]-1, hiker[1], '<'))
    # elif field == 'v':
    #     res.append((hiker[0], hiker[1]+1, 'v'))
    # elif field == '^':
    #     res.append((hiker[0], hiker[1]-1, '^'))
    # normal ground
    if field in '.><v^':
        res.append((hiker[0]+1, hiker[1], '>', []))
        res.append((hiker[0]-1, hiker[1], '<', []))
        res.append((hiker[0], hiker[1]+1, 'v', []))
        res.append((hiker[0], hiker[1]-1, '^', []))
        # remove incoming position / opposite direction
        if dir=='>': res.pop(1)
        elif dir=='<': res.pop(0)
        elif dir=='v': res.pop(3)
        elif dir=='^': res.pop(2)
    
    next=list(filter(lambda x: on_grid(x, grid), res))
    if len(next)>1:
        # memorize fork, so that we don't return here
        fork=pos
        for hi in next:
            hi[3].append(fork)

    return next

def on_grid(pos, grid):
    """ check if position is out of bounds """
    if pos is None: return False
    x=pos[0]
    y=pos[1]
    if x<0: return False
    if y<0: return False
    if x>=len(grid[0]): return False
    if y>=len(grid): return False

    # test ground free (not forest '#')
    if grid[y][x]=='#': return False

    # test step on slope from wrong end
    # dir=pos[2]
    # if grid[y][x]=='>' and dir=='<': return False
    # if grid[y][x]=='<' and dir=='>': return False
    # if grid[y][x]=='v' and dir=='^': return False
    # if grid[y][x]=='^' and dir=='v': return False

    return True

hikers=[] # store x,y,dir
hikers.append( (1,0,'v') )

round=0
while len(hikers)>0 :
    next=[]
    for hiker in hikers:
        next.extend(move_on(hiker, grid))

    round+=1
    hikers=next

    if any(filter(lambda hi: hi[1]==len(grid)-1, hikers)): print(round, len(hikers))

print(round-1)