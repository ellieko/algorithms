'''
101. Symmetric Tree
https://leetcode.com/problems/symmetric-tree/

Given the root of a binary tree, check whether it is a mirror of itself
(i.e., symmetric around its center).
'''

from typing import Optional

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # iterative
    # time complexity: O(n)
    # space complexity: O(logn)
    def isSymmetric_v1(self, root: Optional[TreeNode]) -> bool:
        stack = [(root.left, root.right)]
        while stack:
            l, r = stack.pop()
            if not l and not r:
                continue
            elif not l or not r or l.val != r.val:
                return False
            stack.append((l.left, r.right))
            stack.append((l.right, r.left))
        return True

    # recursive
    # time complexity: O(n)
    # space complexity: O(n)
    def isSymmetric_v2(self, root: Optional[TreeNode]) -> bool:
        def mirror(n1, n2):
            if not n1 and not n2:
                return True
            elif not n1 or not n2 or n1.val != n2.val:
                return False
            return mirror(n1.left, n2.right) and mirror(n1.right, n2.left)
        
        return mirror(root, root)
