'''
323. Number of Connected Components in an Undirected Graph
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

'''

class Solution:
    # recursive dfs
    # time compelxity: O(E+V)
    # space complexity: O(E+V)
    def countComponents_v1(self, n: int, edges) -> int:
        visited = [False] * n
        res = 0
        adj = [[] for i in range(n)]        # O(V)
        for i, j in edges:                  # O(E)
            adj[i].append(j)
            adj[j].append(i)
        
        # during DFS traversal, each vertex will only be visited once
        # when we iterate over the edge list of each vertex, we look at each edge once
        def dfs(i):
            if visited[i]: return
            visited[i] = True
            for node in adj[i]:
                dfs(node)
            
        for i in range(n):
            if visited[i]: continue
            dfs(i)
            res += 1
        return res

    # iterative dfs
    # time complexity: O(E+V)
    # space complexity: O(E+V)
    def countComponents_v2(self, n: int, edges) -> int:
        visited = [False] * n
        adj = [[] for i in range(n)]
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        for i in range(n):
            if visited[i]: continue
            stack = [i]
            while stack:
                n1 = stack.pop()
                visited[n1] = True
                for n2 in adj[n1]:
                    if visited[n2]: continue
                    stack.append(n2)
            res +=1

        return res

    # iterative bfs
    # time complexity:
    # space complexity:
