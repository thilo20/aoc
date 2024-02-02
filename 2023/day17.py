import re

total=0
grid=[] # store tile(x,y) -> grid[y][x]

# Opening file
file = open('2023/day17-test.txt', 'r')
for line in file:
    grid.append(list(map(lambda x: int(x), re.findall("\d", line))))
file.close()

class Node:
    def __init__(self, parent, x, y, dir, cost):
      self.parent=parent
      self.x=x
      self.y=y
      self.dir=dir
      self.cost=cost
      self.heu=0

    def __str__(self):
        return f"{self.x} {self.y} {self.dir} {self.cost} {self.heu})"
    
    def __eq__(self, other: object) -> bool:
        """ compare attributes x,y,dir """
        if isinstance(other, self.__class__):
            return (self.x == other.x) and (self.y == other.y) and (self.dir == other.dir)
        else:
            return False
        
    def addcost(self, cost):
        self.cost+=cost
    
    def parents(self):
        i=0
        p=self.parent
        while p is not None:
            p=p.parent
            i+=1
        return i

def expand(node, grid):
    """ return list of possible next moves """
    moves=[]
    # init all 4 moves
    moves.append(Node(node, node.x+1, node.y, '>', node.cost))
    # moves.append(Node(node, node.x-1, node.y, '<', node.cost))
    moves.append(Node(node, node.x, node.y+1, 'v', node.cost))
    # moves.append(Node(node, node.x, node.y-1, '^', node.cost))
    # remove opposite direction
    opposite={ '>':1, '<':0, 'v':3, '^':2}
    # moves.pop(opposite[node.dir])

    moves = list(filter(lambda n: on_grid(n.x, n.y, grid), moves))
    for m in moves:
        m.addcost(grid[m.y][m.x])
        m.heu=dist(m.x, m.y, grid)
    return moves

def on_grid(x, y, grid):
    """ check if position is out of bounds """
    if x<0: return False
    if y<0: return False
    if x>=len(grid[0]): return False
    if y>=len(grid): return False
    return True

def dist(x, y, grid):
    """ calculate manhattan distance """
    return abs(len(grid)-y) + abs(len(grid[0])-x)

max=len(grid)-1
start=Node(None, 0,0,'>',0)
dest=Node(None, max,max,'',-1)

openlist=[] # store x,y,dir,cost
openlist.append( start )

closedlist=[]

while len(openlist)>0 :
    node=openlist.pop()

    if node.x==dest.x and node.y==dest.y:
        print("cost=", node.cost)
        break

    next=expand(node, grid)
    
    for n in next:
        if n not in closedlist: 
            openlist.append(n)
        else:
            i = closedlist.index(n)
            n2=closedlist[i]
            # update costs
            if n.cost < n2.cost:
                closedlist[i]=n

    if node not in closedlist:
        closedlist.append(node)

msg="open: {} closed: {}"
print(msg.format(len(openlist), len(closedlist)))

print(total)

    # "git.path": "/usr/bin/git",
    # "git.enabled": true
