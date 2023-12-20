
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
