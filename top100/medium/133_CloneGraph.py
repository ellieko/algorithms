'''
133. Clone Graph
https://leetcode.com/problems/clone-graph/

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

'''


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    # dfs
    # time complexity: O(N+M) where N is a number of vertices and M is a number of edges
    # space complexity: O(N)
    # this space is occupied by the visited hash map and
    # in addition to that, space would also be occupied by the recursion stack
    # The space occupied by the recursion stack would be equal to O(H) where H is the height of the graph.
    # Overall, the space complexity would be O(N)
    def cloneGraph_v1(self, node: 'Node') -> 'Node':
        oldToNew = {}
        
        def clone(node):
            if not node: return None
            
            if node not in oldToNew:
                oldToNew[node] = Node(node.val)                
                for nei in node.neighbors:
                    oldToNew[node].neighbors.append(clone(nei))
                    
            return oldToNew[node]
            
        return clone(node)

    # bfs
    # time complexity: O(N+M)
    # space complexity: O(N)
    # this space is occupied by the visited dictionary and
    # in addition to that, space would also be occupied by the queue
    # The space occupied by the queue would be equal to O(W) where W is the width of the graph
    # Overall, the space complexity would be O(N)
    def cloneGraph_v2(self, node: 'Node') -> 'Node':
        from collections import deque

        if not node: return None

        q = deque([node])
        oldToNew = {node: Node(node.val)}

        while q:
            n = q.popleft()
            for nei in n.neighbors:
                if nei not in oldToNew:
                    oldToNew[nei] = Node(nei.val)
                    q.append(nei)
                oldToNew[n].neighbors.append(oldToNew[nei])

        return oldToNew[node]
