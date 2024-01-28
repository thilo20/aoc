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
            print("queue", queue)
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
        

if __name__ == "__main__":
    solution = Solution()
    image = [
        [1, 1, 1, 0, 1],
        [1, 0, 1, 1, 0],
        [1, 1, 1, 0, 1],
        [1, 1, 0, 1, 1],
    ]
    sr = 2
    sc = 2
    newColor = 2
    print("flood fill result", solution.floodFill(image, sr, sc, newColor))
