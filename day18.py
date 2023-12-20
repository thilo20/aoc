
total=0

plan=[] # (x,y) digged out
start=(0,0)
pos=start

dir={'U': (0,-1), 'D': (0,1), 'L': (-1,0), 'R': (1,0)}

# Opening file
file = open('day18.txt', 'r')
for line in file:
    command=line.split()
    d=dir[command[0]]
    steps=int(command[1])
    while steps>0:
        #pos+=d
        pos=tuple(sum(x) for x in zip(pos, d))
        plan.append(pos)
        steps-=1
file.close()

# calc bounds and create image
minx=min(map(lambda x:x[0],plan))
miny=min(map(lambda x:x[1],plan))
maxx=max(map(lambda x:x[0],plan))
maxy=max(map(lambda x:x[1],plan))
dimy=maxy-miny+1
dimx=maxx-minx+1
image=[]
for y in range(dimy):
    image.append([0]*dimx)
for dig in plan:
    image[dig[1]-miny][dig[0]-minx]=1

total=sum([sum(x) for x in image])
print(total)

# find start pos
# for i in range(dimx):
#      if image[0][i]>0: print(i)
# 127,1

# https://gist.github.com/shkolovy/a2c807e5ba2783ded3eedd55b9abf42c
from queue import Queue
def get_neightbs(array, pos):
    neighbs = []

    if pos[1] > 0:
        neighbs.append((pos[0], pos[1] - 1))
    if pos[0] > 0:
        neighbs.append((pos[0] - 1, pos[1]))
    if pos[1] < len(array[0]) - 1:
        neighbs.append((pos[0], pos[1] + 1))
    if pos[0] < len(array) - 1:
        neighbs.append((pos[0] + 1, pos[1]))

    return neighbs

#pos (1,2) row, col
def flood_fill(array, start_pos):
    q = Queue()
    q.put(start_pos)
    val=array[start_pos[0]][start_pos[1]]

    while not q.empty():
        pos = q.get()
        array[pos[0]][pos[1]] = val

        neighbs = get_neightbs(array, pos)
        for n in neighbs:
            if array[n[0]][n[1]] == 0:
                q.put(n)

# flood_fill(image, (1,1))

# from https://lvngd.com/blog/flood-fill-algorithm-python/
def flood_recursive(matrix, start_pos):
	width = len(matrix)
	height = len(matrix[0])
        
	def fill(x,y,start_color,color_to_update):
		#if the square is not the same color as the starting point
		if matrix[x][y] != start_color:
			return
		#if the square is not the new color
		elif matrix[x][y] == color_to_update:
			return
		else:
			#update the color of the current square to the replacement color
			matrix[x][y] = color_to_update
			neighbors = [(x-1,y),(x+1,y),(x-1,y-1),(x+1,y+1),(x-1,y+1),(x+1,y-1),(x,y-1),(x,y+1)]
			for n in neighbors:
				if 0 <= n[0] <= width-1 and 0 <= n[1] <= height-1:
					fill(n[0],n[1],start_color,color_to_update)
	start_x = start_pos[0]
	start_y = start_pos[1]
	start_color = matrix[start_x][start_y]
	fill(start_x,start_y,start_color,1)
	return matrix

# flood_recursive(image, (1,1))
# fails with RecursionError: maximum recursion depth exceeded

# https://yuminlee2.medium.com/flood-seed-fill-algorithm-21fba08a46e#9537

from collections import deque
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image
        
        visited = set([(sr, sc)])
        queue = deque([(sr, sc)])

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while len(queue) > 0:
            # print("queue", queue)
            currentRow, currentCol = queue.popleft()
            image[currentRow][currentCol] = newColor
            for rowOffset, colOffset in directions:
                neighborRow = currentRow + rowOffset
                neighborCol = currentCol + colOffset
                pos = (neighborRow, neighborCol)
                if self.isInBounds(image, neighborRow, neighborCol) and pos not in visited and image[neighborRow][neighborCol] == oldColor:
                    visited.add(pos)
                    queue.append((neighborRow, neighborCol))
        
        return image
    
    def isInBounds(self, image, row, col):
        return 0 <= row < len(image) and 0 <= col < len(image[0])

solution=Solution()
sr = 1
sc = 127
newColor = 1
image=solution.floodFill(image, sr, sc, newColor)

total=sum([sum(x) for x in image])
print(total)
