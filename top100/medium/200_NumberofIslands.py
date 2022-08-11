'''
200. Number of Islands
https://leetcode.com/problems/number-of-islands/

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

'''

class Solution:
    # make sure to check input type... grid consists of string "1" and "0" not integers

    # dfs + modifying the grid
    # time complexity: O(M*N) where M is the number of rows and N is the number of columns.
    # space complexity: O(M,N) because in worst case where the grid is filled with lands ("1"),
    # where DFS goes by M*N deep
    def numIslands_v1(self, grid) -> int:
        # dfs
        def dfs(i, j):
            if (i < 0 or i >= len(grid) or
                j < 0 or j >= len(grid[0]) or
                grid[i][j] == "0"):
                return
            grid[i][j] = "0"       
            for r,c in (0, 1), (0, -1), (1, 0), (-1, 0):
                dfs(i+r, j+c)     
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    islands += 1
        return islands

    # dfs + having an extra memory for visit (instead of modifying the grid)
    # time complexity: O(M*N)
    # space complexity: O(M*N) - I think? worst case when the grid is filled with lands (visit)
    def numIslands_v2(self, grid) -> int:
        visit = set()
        islands = 0

        # dfs
        def dfs(i, j):
            if (i not in range(len(grid)) or            # if i is not a valid index
                j not in range(len(grid[0])) or         # if j is not a valid index
                grid[i][j] == "0" or                    # if it's water that we cannot visit to
                (i, j) in visit):                       # if we've already visited this land
                return

            visit.add((i, j))                           # mark that we're visiting (i, j)
            for r,c in (0, 1), (0, -1), (1, 0), (-1, 0):
                dfs(i+r, j+c)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visit:
                    dfs(i, j)   # actually calling dfs function (don't forget!)
                    islands += 1
        return islands

    # bfs + modifying the grid
    # time complexity: O(M*N)
    # space complexity: O(min(M,N)) because in worst case where the grid is filled with lands ("1"),
    # the size of queue can grow up to min(M,N)
    # (maximum siblings in queue will be min(M, N))
    def numIslands_v3(self, grid) -> int:
        from collections import deque
        islands = 0
        
        def bfs(i, j):
            q = deque([(i,j)])
            while q:
                i, j = q.popleft()
                if (i not in range(len(grid)) or 
                    j not in range(len(grid[0])) or
                    grid[i][j] == "0"): continue
                
                grid[i][j] = "0"       # mark we're visiting (i, j)
                for r,c in (0, 1), (0, -1), (1, 0), (-1, 0):
                    q.append((i+r, j+c))
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    bfs(i,j)
                    islands += 1
        return islands