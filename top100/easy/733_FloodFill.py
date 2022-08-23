'''
733. Flood Fill
https://leetcode.com/problems/flood-fill/

'''

from collections import deque
from typing import List


class Solution:

    # bfs
    # time complexity: O(n*m)
    # space complexity: O(n+m) - ????
    def floodFill_bfs(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        # change all neighbor grids of the grid (sr, sc) whose color is fromColor
        # to have toColor
        fromColor = image[sr][sc]
        toColor = color
        q = deque([(sr, sc)])
        visited = set()     # do we need this? 
        
        while q:
            for i in range(len(q)):
                i, j = q.popleft()
                if (i < 0 or j < 0 or i >= len(image) or j >= len(image[0])
                    or image[i][j] != fromColor or (i, j) in visited):
                    continue
                visited.add((i, j))
                image[i][j] = toColor
                for r,c in (0, 1), (0, -1), (1, 0), (-1, 0):
                    q.append((i+r, j+c))
                    
        return image


    # dfs
    # time complexity: O(n*m)
    # space complexity: (n*m)
    def floodFill_dfs(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        from_color = image[sr][sc]
        to_color = color
        
        if from_color == to_color:
            return image
        
        n = len(image[0])  # width 
        m = len(image)     # height
        
        def dfs(i,j):
        
            if image[i][j] == from_color:
                image[i][j] = to_color
                for step in [(1,0),(-1,0), (0,1), (0,-1)]:
                    x = i + step[0]
                    y = j + step[1]
                    if x >= 0 and x < m and y >= 0 and y < n:
                        dfs(x, y)
            
        dfs(sr, sc)
        return image