import re
import heapq

total=1e12
grid=[] # store tile(x,y) -> grid[y][x]

# Opening file
file = open('2023/day17.txt', 'r')
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
      self.samedir=0

    def __str__(self):
        return f"{self.x} {self.y} {self.dir} {self.cost} {self.heu}"
    
    def __eq__(self, other: object) -> bool:
        """ compare attributes x,y,dir,samedir """
        if isinstance(other, self.__class__):
            return (self.x == other.x) and (self.y == other.y) and (self.dir == other.dir) and (self.samedir == other.samedir)
        else:
            return False
        
    def __lt__(self, other) -> bool:
        """ low heuristic value means close to target. high priority, compare lower """
        return self.cost+self.heu < other.cost+other.heu
    
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
    moves.append(Node(node, node.x-1, node.y, '<', node.cost))
    moves.append(Node(node, node.x, node.y+1, 'v', node.cost))
    moves.append(Node(node, node.x, node.y-1, '^', node.cost))
    # remove opposite direction
    opposite={ '>':1, '<':0, 'v':3, '^':2}
    moves.pop(opposite[node.dir])

    moves = list(filter(lambda n: on_grid(n.x, n.y, grid), moves))
    for m in moves:
        m.cost+=grid[m.y][m.x]
        m.heu=dist(m.x, m.y, dest)*2
        if node.dir==m.dir:
            m.samedir=node.samedir+1

    moves = list(filter(lambda n: n.samedir<3, moves))
    return moves

def on_grid(x, y, grid):
    """ check if position is out of bounds """
    if x<0: return False
    if y<0: return False
    if x>=len(grid[0]): return False
    if y>=len(grid): return False
    return True

def dist(x, y, dest):
    """ calculate manhattan distance """
    return abs(dest.y-y) + abs(dest.x-x)

max=len(grid)-1
start=Node(None, 0,0,'>',0)
dest=Node(None, max,max,'',-1)
# dest=Node(None, 30,30,'',-1)

start2=Node(None, 0,0,'>',0)
start2.samedir=3
assert start != start2, "nodes must not compare equal!"

openlist=[] # store x,y,dir,cost
# openlist.append( start )
heapq.heappush(openlist, start)

closedlist=[]
p=0
while len(openlist)>0 :
    p+=1
    if p%1000==0: print(f"open:{len(openlist)} closed:{len(closedlist)}")

    # node=openlist.pop()
    node=heapq.heappop(openlist)
    # heapq.heapify(openlist)

    if node.x==dest.x and node.y==dest.y:
        print(f"node={node} parents={node.parents()}")
        total=min(total,node.cost)
        break

    # if node not in closedlist:
    closedlist.append(node)
    
    next=expand(node, grid)
    for n in next:
        if n not in closedlist: 
            if n not in openlist:
                # openlist.append(n)
                heapq.heappush(openlist, n)
            else:
                i = openlist.index(n)
                n2= openlist[i]
                # update costs
                if n.cost < n2.cost:
                    print(f"better cost: {n} vs. {n2} open={len(openlist)} closed={len(closedlist)}")
                    openlist.pop(i)
                    heapq.heappush(openlist, n)


msg="open: {} closed: {}"
print(msg.format(len(openlist), len(closedlist)))
print(f"steps: {node.parents()}")
print(total)
