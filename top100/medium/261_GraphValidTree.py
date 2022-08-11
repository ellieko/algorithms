'''
261. Graph Valid Tree
https://leetcode.com/problems/graph-valid-tree/

'''

class Solution:
    # valid tree: fully connected w/o any loops(cycles)
    # recursive dfs
    # time complexity: O(N+E)
    # space complexity: O(N+E)
    def validTree_v1(self, n: int, edges) -> bool:
        
        visited = set()
        adj = {i:[] for i in range(n)}
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
            
        def dfs(node, prev):
            if node in visited: return False    # detecting a loop 
            visited.add(node)
            for edge in adj[node]:
                if edge == prev: continue
                if not dfs(edge, node):
                    return False
            return True
        
        # if it doesn't include a loop (cycle) and fully connected graph
        return dfs(0, -1) and len(visited) == n 


    # The recursive approach is more elegant,
    # but is considered inferior to the iterative version in some programming languages, such as Python.
    # This is because the space used by run-time stacks vary between programming languages.
    
    # iterative dfs
    # make sure not to use the pre-defined (input or used above) variables!!!!!
    def validTree_v2(self, n: int, edges) -> bool:
        adj = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()
        stack = [(0,-1)]
        
        while stack:
            n1, prev = stack.pop()
            visited.add(n1)
            for n2 in adj[n1]:
                if n2 == prev: continue
                if n2 in visited:
                    return False
                stack.append((n2, n1))

        return len(visited) == n 

    # iterative bfs
    # almost identical to iterative dfs but with different data strcuture (queue instead of stack)
    def validTree_v3(self, n: int, edges) -> bool:
        from collections import deque
        adj = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()
        q = deque([(0,-1)])
        
        while q:
            n1, prev = q.popleft()
            visited.add(n1)
            for n2 in adj[n1]:
                if n2 == prev: continue
                if n2 in visited:
                    return False
                q.append((n2, n1))

        return len(visited) == n


    # another approach using advanced graph theory

    # for the graph to be a valid tree
    # it must have exactly n - 1 edges
    # any less, and it can't possibly be fully connected, any more, and it has to contain cycles
    # if the graph is fully connected and contains exactly n - 1 edges, it can't possibly contain a cycle -> must be a tree

    # which means even if it has n - 1 edges, we still have to check it's fully connected

    # check the number of edges and check whether the graph is fully connected

    # We still need to use a seen set to prevent the algorithm getting caught in an infinite loop
    # if there are indeed cycles (and to prevent looping on the trivial cycles)


    # time complexity: O(N) because the worst case is when E = N - 1, O(N + E) = O(N)
    # space complexity: O(N)
    # O(N) for adjacency list and
    # O(N) for the worst case when the search algorithms require an additional O(N) space
    #      (if all nodes were on the stack/queue at the same time)
    def validTree_v4(self, n: int, edges) -> bool:
        if len(edges) != n - 1:  return False
        adj = [[] for i in range(n)]            # doesn't need to be dict
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        stack, visited = [0], {}
        while stack:
            n1 = stack.pop()
            visited.add(n1)
            for n2 in adj[n1]:
                if n2 in visited:
                    continue
                stack.append(n2)
        
        return len(visited) == n


