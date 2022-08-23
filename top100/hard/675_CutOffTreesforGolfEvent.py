'''
675. Cut Off Trees for Golf Event
https://leetcode.com/problems/cut-off-trees-for-golf-event/

https://leetcode.com/problems/cut-off-trees-for-golf-event/discuss/107396/Python-solution-based-on-wufangjie's-(Hadlock's-algorithm)

'''

from typing import List
from collections import deque


class Solution:

    # problem: misunderstanding the problem
    # every time we visit node, we "can choose to cut off the tree or not"
    # (we can cut off the tree later if that makes everything to be cut off)
    # 1 7 6
    # 0 0 5
    # 2 3 4 
    # i thought it should return -1 but what it's supposed to return is 11
    # by choosing not cutting off trees in the first time they visit the node...
    # let's finish up the question later

    # 21 / 55 test cases passed.
    def cutOffTree_bfs(self, forest: List[List[int]]) -> int:
        m, n = len(forest), len(forest[0])
        res = 0
        q = deque([(0, 0, -1)])
        visited = set()

        while q:
            for i in range(len(q)):
                i, j, prev = q.pop()
                if (i < 0 or j < 0 or i >= m or j >= n or
                    (i, j) in visited or forest[i][j] == 0):
                    continue
                if forest[i][j] == 1 or prev < forest[i][j]:
                    visited.add((i, j))
                    for r, c in (0, 1), (0, -1), (1, 0), (-1, 0):
                        q.append((i+r, j+c, prev))
                if forest[i][j] > 1:
                    res = res + 0 if i == 0 and j == 0 else res + 1
                    prev = forest[i][j]

        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    return -1
        return res
        

    # 21 / 55 test cases passed.
    def cutOffTree_dfs(self, forest: List[List[int]]) -> int:
        m, n = len(forest), len(forest[0])
        self.cut = 0
        
        def dfs(i, j, prev):
            # cannot walk through
            if i < 0 or j < 0 or i >= m or j >= n or forest[i][j] == 0 or forest[i][j] <= prev :
                return
            # can work through
            if forest[i][j] > 1:
                if (i,j) != (0,0):
                    self.cut += 1
                prev = forest[i][j]
                forest[i][j] = 1
                
            for r, c in (0, 1), (0, -1), (1, 0), (-1, 0):
                dfs(i+r, j+c, prev)
        
        dfs(0, 0, -1)
        
        for i in range(m):
            for j in range(n):
                if forest[i][j] not in (0, 1):
                    return -1