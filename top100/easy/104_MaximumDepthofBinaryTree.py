'''
104. Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/


Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes
along the longest path from the root node down to the farthest leaf node.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # recursive approach (DFS)
    # time complexity: O(n)
    # space complexity: O(n)
    def maxDepth_v1(self, root) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # iterative approach (DFS) - pre order traversal (root -> left -> right)
    # time complexity: O(n)
    # space complexity: O(n)
    def maxDepth_v2(self, root) -> int:
        max_depth = 0
        stack = [(root, 1)]
        while stack:
            node, depth = stack.pop()
            if node:
                max_depth = max(max_depth, depth)
                stack.append((node.left, depth+1))
                stack.append((node.right, depth+1))
        return max_depth
        

    # iterative approach (BFS) - level order traversal
    # time complexity: O(n)
    # space complexity: O(n)
    def maxDepth_v3(self, root) -> int:
        from collections import deque
        if not root:
            return 0

        q = deque([root])
        level = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level


