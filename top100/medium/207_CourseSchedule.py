'''
207. Course Schedule
https://leetcode.com/problems/course-schedule/

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi]
indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

'''

class Solution:
    # time comoplexity: O(V+P)
    # space complexity: O(V+P)

    def canFinish(self, numCourses: int, prerequisites) -> bool:
        
        # { course: a list of its prerequisites }
        preMap = {i:[] for i in range(numCourses)}
        visited = set()
        
        for crs,pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(crs):
            if crs in visited:
                return False
            if preMap[crs] == []:
                return True

            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            preMap[crs] = []
            
            return True
        
        for crs,pre in prerequisites:
            if not dfs(crs):
                return False
            
        return True
        