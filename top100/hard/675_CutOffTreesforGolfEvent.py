'''
675. Cut Off Trees for Golf Event
https://leetcode.com/problems/cut-off-trees-for-golf-event/

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

    # 33/55 test cases passed... Rest: TLE
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m, n = len(forest), len(forest[0])
        sorted_array = [c for row in forest for c in row]
        for i in range(m):
            if set(forest[i]) == {0}:
                return -1
            
        sorted_array.sort()
        print(sorted_array)

        # (r, c): current position
        # (x, y): target position
        # can we get there?
        # if so, how many steps?
        def bfs(r, c, x, y) -> int:
            res = 0

            visited = set()
            q = deque([(r, c)])
            while q:
                for i in range(len(q)):
                    curR, curC = q.popleft()
                    visited.add((curR, curC))
                    if curR == x and curC == y:
                        return res
                    for changeR, changeC in (0, 1), (0, -1), (1, 0), (-1, 0):
                        newR, newC = curR + changeR, curC + changeC
                        if (newR < 0 or newC < 0 or newR >= m or newC >= n or
                            (newR, newC) in visited or forest[newR][newC] == 0):
                            continue
                        q.append((newR, newC))   
                    # when i'm supposed to increment and decrement res...
                    # currently even if i failed to find the steps, still step is added...
                res +=1

            return -1

        r = c = steps = 0
        for idx in range(len(sorted_array)):
            if sorted_array[idx] > 0:
                x = y = 0
                for i, row in enumerate(forest):
                    if sorted_array[idx] in row:
                        x, y = i, row.index(sorted_array[idx])
                        print(f"FOUND X and Y = {x} and {y}")
                        break

                # check if we can reach to from (r, c) to (x, y)
                # print(f"(r, c) = {(r, c)} and (x, y) = {(x, y)}")
                if (r, c) == (x, y):
                    continue 

                res = bfs(r, c, x, y)
                if res == -1:
                    return -1
                print(f"res = {res}")
                steps += res
                print(f"steps = {steps}")
                r, c = x, y
                
        return steps


               

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

if __name__ == '__main__':
    l = [[1,7,6],[0,0,5],[2,3,4]]
    print(Solution().cutOffTree(l))