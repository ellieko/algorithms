from collections import deque


class Solution:
    # BFS
    # time complexity: O(N) where N is the size of the grid
    # we run the BFS process on the queue, which in the worst case
    # would enumerate all the cells in the grid once and only once. -> O(N)
    # not fully understood this worst case scenario...!!!!!!!

    # space complexity: O(N) O(N), where NN is the size of the grid.
    # In the worst case, the grid is filled with rotten oranges.

    def orangesRotting(self, grid) -> int:
        
        n, m = len(grid), len(grid[0])
        rottens = deque()
        fresh_oranges = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    rottens.append((i, j))
                elif grid[i][j] == 1:
                    fresh_oranges += 1
        
                
        times = 0 
        while rottens and fresh_oranges > 0:

            for i in range(len(rottens)):
                x,y = rottens.popleft()
                for dr, dc in (0,1), (0,-1), (1,0), (-1,0):
                    nr, nc = x+dr, y+dc
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        rottens.append((nr, nc))
                        fresh_oranges -= 1
            times += 1

        return times if fresh_oranges == 0 else -1
        