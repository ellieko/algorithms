'''
207. Course Schedule
https://leetcode.com/problems/course-schedule/

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi]
indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

'''

from typing import List


class Solution:
    # time complexity: O(v+e)
    # space complexity: O(v+e)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # cannot use defaultdict(list),
        # it gives RuntimeError: dictionaty chanced size during iteration
        # { course: a list of its prerequisites }
        adj = {i:[] for i in range(numCourses)}
        
        for crs, pre in prerequisites:
            adj[crs].append(pre)
            
        visited = set()
        
        def dfs(crs):
            if crs in visited:      # cycle detected
                return False
            if adj[crs] == []:
                return True
            
            visited.add(crs)
            for pre in adj[crs]:
                if not dfs(pre): return False
            visited.remove(crs)
            adj[crs] = []
            return True
            
        
        for i in range(numCourses):
            if not dfs(i): return False
                
        return True
        