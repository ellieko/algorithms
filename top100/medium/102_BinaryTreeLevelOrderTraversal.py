'''
102. Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/

Given the root of a binary tree,
return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # BFS (queue, first in first out)
    # time complexity: O(n) since each node is processed exactly once
    # space complexity: O(n) to keep the output structure which contains N node values
    def levelOrder(self, root):
        from collections import deque
        q = deque([root])
        res = []
        
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        
        return res
            