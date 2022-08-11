'''
417. Pacific Atlantic Water Flow
https://leetcode.com/problems/pacific-atlantic-water-flow/

'''

class Solution:
    
    # dfs
    # time complexity: O(N*M) where N*M is the size of heights
    # dfs function runs exactly once for each cell accessible from an ocean
    # space complexity: O(N*M)
    # space used by dfs calls on the recursion stack

    def pacificAtlantic(self, heights):
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        
        def dfs(i, j, visited, prevHeight):
            if (i not in range(ROWS) or
                j not in range(COLS) or
                (i, j) in visited or
                prevHeight > heights[i][j]): return
            
            visited.add((i, j))
            for r, c in (0, 1), (0, -1), (1, 0), (-1, 0):
                dfs(i+r, j+c, visited, heights[i][j])
                
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])
                    
        return list(pac.intersection(atl))

    # bfs
    # time complexity: O(N*M) where N*M is the size of heights
    # In the worst case, such as a matrix where every value is equal, we would visit every cell twice
    # This is because we perform 2 traversals, and during each traversal, we visit each cell exactly once
    # There are M*N cells total, which gives us a time complexity of O(2*M*N)= O(M⋅N)
    # space complexity: O(N*M)
    # space used by queue

    def pacificAtlantic(self, heights):
        from collections import deque
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = deque(), deque()
        
        def bfs(q):
            visited = set()
            
            while q:
                i, j = q.popleft()

                visited.add((i, j))
                for r, c in (0, 1), (0, -1), (1, 0), (-1, 0):
                    new_row, new_col = i+r, j+c
                    if (new_row < 0 or new_col < 0 or
                        new_row == ROWS or new_col == COLS or
                        (new_row, new_col) in visited or
                        heights[i][j] > heights[new_row][new_col]):
                        continue
                    q.append((new_row, new_col))
                    
            return visited
                
        for r in range(ROWS):
            pac.append((r, 0))
            atl.append((r, COLS-1))

        for c in range(COLS):
            pac.append((0, c))
            atl.append((ROWS-1, c))
        
        return list(bfs(pac).intersection(bfs(atl)))