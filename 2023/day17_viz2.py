# extended day17.py by visualization, inspired by day17_viz.py

import re
import heapq

grid=[] # store tile(x,y) -> grid[y][x]

from typing import Any, Callable, List, Dict, NamedTuple, Optional, Set, Tuple

def read_input(filename: str) -> List[List[int]]:
    with open(filename, "r") as f:
        return [list(map(int, list(line.strip()))) for line in f.readlines()]

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
            return (self.x == other.x) and (self.y == other.y) #and (self.dir == other.dir) and (self.samedir == other.samedir)
        else:
            return False
        
    def __lt__(self, other) -> bool:
        """ low heuristic value means close to target. high priority, compare lower """
        return self.cost+self.heu < other.cost+other.heu
        # return self.cost < other.cost
    
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
        m.heu=dist(m.x, m.y, dest)*1
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
# assert start != start2, "nodes must not compare equal!"

openlist=[] # store x,y,dir,cost
# openlist.append( start )
heapq.heappush(openlist, start)

import pygame
import os
pygame.font.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FONT_SIZE = 6
FONT = pygame.font.SysFont("Arial", 18)
CLOCK = None

FPS = 120
VEL = 5


COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_YELLOW = (255, 255, 0)
COLOR_GREEN = (0, 255, 0)

TITLE = "AoC 2023 - Day 17 - Clumsy Crucible"

import time

def find_shortest_path(grid):
    total=1e12
    time_start=time.time() # time elapsed since epoch, in s

    closedlist=[]
    p=0
    while len(openlist)>0 :
        # node=openlist.pop()
        node=heapq.heappop(openlist)
        # heapq.heapify(openlist)

        if node.x==dest.x and node.y==dest.y:
            print(f"node={node} parents={node.parents()}")
            total=min(total,node.cost)
            break

        coord=(node.x, node.y)
        pygame.draw.rect(WIN, COLOR_RED, (coord[0] * FONT_SIZE, coord[1] * FONT_SIZE, FONT_SIZE, FONT_SIZE))
        pygame.display.update()

        # if node not in closedlist:
        closedlist.append(node)
        
        next=expand(node, grid)
        for n in next:
            if n not in closedlist: 
                if n not in openlist:
                    # openlist.append(n)
                    heapq.heappush(openlist, n)

                    new_coord=(n.x, n.y)
                    pygame.draw.rect(
                        WIN, COLOR_YELLOW, (new_coord[0] * FONT_SIZE, new_coord[1] * FONT_SIZE, FONT_SIZE, FONT_SIZE)
                    )

                else:
                    i = openlist.index(n)
                    n2= openlist[i]
                    # update costs
                    if n.cost < n2.cost:
                        # print(f"better cost: {n} vs. {n2} open={len(openlist)} closed={len(closedlist)}")
                        openlist.pop(i)
                        heapq.heappush(openlist, n)

        p+=1
        if p%1000==0: print(f"open:{len(openlist)} closed:{len(closedlist)} time:{time.time()-time_start}")

    msg="open: {} closed: {}"
    print(msg.format(len(openlist), len(closedlist)))
    print(f"steps: {node.parents()}")
    print(total)
    time_total=time.time()-time_start
    print(f"time total: {time_total} s or {time_total/60} min")


def init_window(matrix: List[List[int]]) -> None:
    global WIN, FONT, CLOCK, WIDTH, HEIGHT, FONT_SIZE

    # FONT_SIZE = 9
    WIDTH, HEIGHT = len(matrix[0]) * FONT_SIZE, len(matrix) * FONT_SIZE
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(f"{TITLE} - PRESS [SPACE] TO START")
    FONT = pygame.font.SysFont("Arial", FONT_SIZE)
    CLOCK = pygame.time.Clock()
    WIN.fill(COLOR_BLACK)
    draw_matrix(matrix)
    pygame.display.update()

def draw_matrix(matrix: List[List[int]]) -> None:
    for y, line in enumerate(matrix):
        for x, value in enumerate(line):
            comp = int(255 / 16 * (16 - value))
            color = (comp, comp, comp)
            pygame.draw.rect(WIN, color, (x * FONT_SIZE, y * FONT_SIZE, FONT_SIZE, FONT_SIZE))

def main():
    input_filename = f"2023/day17.txt"
    # input_filename = f"day_{DAY}_input_sample.txt"
    matrix = read_input(input_filename)
    init_window(matrix)

    run = True
    while run:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                find_shortest_path(matrix)


if __name__ == "__main__":
    main()
