'''
103. Binary Tree Zigzag Level Order Traversal
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

Given the root of a binary tree,
return the zigzag level order traversal of its nodes' values.
(i.e., from left to right, then right to left for the next level and alternate between).

'''

# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # time complexity: O(n) where n is the number of nodes in the tree
    # we visit each node once and only once

    # space complexity: O(n) from our queue (q)
    # no more than 2 * (maximum number of nodes that might reside on the same level)
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res, direction = [], True
        q = deque([root])
        while q:
            level = deque()
            for _ in range(len(q)):
                node = q.popleft()
                if not node: continue
                if direction:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                q.append(node.left)
                q.append(node.right)
            direction = not direction
            if level:
                res.append(level)
        return res