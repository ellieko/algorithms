'''
542. 01 Matrix
https://leetcode.com/problems/01-matrix/ 

'''

class Solution:
    # BFS
    # Time Limit Exceeded
    # time & space complexity: O(R*C)
    def updateMatrix_v1(self, mat):
        
        n, m = len(mat[0]), len(mat)
        # n is width, m is height
        
        max_int = 2*pow(10, 4)
        dist = [[max_int]*n for _ in range(m)]
                
        zeros_at = []
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    zeros_at.append((i, j))
                    
        while zeros_at:
            zero_i, zero_j = zeros_at.pop()
            for step in [(-1,0), (1,0), (0,1), (0,-1)]:
                x, y = zero_i+step[0], zero_j+step[1]
                if x >= 0 and x < m and y >= 0 and y < n:
                    if dist[x][y] > dist[zero_i][zero_j] + 1:
                        dist[x][y] = dist[zero_i][zero_j] + 1
                        zeros_at.append((x, y))
        return dist

    def updateMatrix_v2(self, mat):
        # n is width, m is height
        n, m = len(mat[0]), len(mat)
        q = []

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i,j))
                else:
                    mat[i][j] = '#'
                    
        for r,c in q:
            for step in (-1,0), (1,0), (0,1), (0,-1):
                nr, nc = r+step[0], c+step[1]
                if 0 <= nr < m and 0 <= nc < n and mat[nr][nc] == '#':
                    mat[nr][nc] = mat[r][c] + 1
                    q.append((nr, nc))
                    
        return mat