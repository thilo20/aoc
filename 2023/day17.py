import re

total=0
grid=[] # store tile(x,y) -> grid[y][x]

# Opening file
file = open('day17-test.txt', 'r')
for line in file:
    grid.append(list(map(lambda x: int(x), re.findall("\d", line))))
file.close()

class Node:
    def __init__(self, x, y, dir, cost):
      self.x=x
      self.y=y
      self.dir=dir
      self.cost=cost

    def __str__(self):
        return f"{self.x} {self.y} {self.dir} {self.cost})"

def expand(node, tile):
    """ return list of possible next moves """
    cost=tile[node.y][node.x]
    moves=[]
    # init all 4 moves
    moves.append(Node(node.x+1, node.y, '>', node.cost))
    moves.append(Node(node.x-1, node.y, '<', node.cost))
    moves.append(Node(node.x, node.y+1, 'v', node.cost))
    moves.append(Node(node.x, node.y-1, '^', node.cost))
    # remove opposite direction
    opposite={ '>':1, '<':0, 'v':3, '^':2}
    moves.pop(opposite[node.dir])

    return list(filter(lambda n: on_grid(n.x, n.y, tile), moves))

def on_grid(x, y, grid):
    """ check if position is out of bounds """
    if x<0: return False
    if y<0: return False
    if x>=len(grid[0]): return False
    if y>=len(grid): return False
    return True

max=len(grid)-1
start=Node(0,0,'>',0)
dest=Node(max,max,'',-1)

openlist=[] # store x,y,dir,cost
openlist.append( start )

closedlist=[]

while len(openlist)>0 :
    node=openlist.pop()

    if node.x==dest.x and node.y==dest.y:
        print("cost=", node.cost)

    next=expand(node, grid)
    
    for n in next:
        find
        if n not in closedlist: 
            openlist.append(n)

    if node not in closedlist:
        closedlist.append(node)

msg="open: {} closed: {}"
print(msg.format(len(openlist), len(closedlist)))

print(total)