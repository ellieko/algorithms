'''
100. Same Tree

Given the roots of two binary trees p and q,
write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical,
and the nodes have the same value.

'''

from tkinter import SOLID
from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # approach 1) recursion
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:     # both are None     --> True
            return True
        elif not p or not q:    # only one is None  --> False
            return False
        elif p.val != q.val:    # have diff val     --> False
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    # approach 2) iteration
    def isSameTree_v2(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(p, q):
            if not p and not q:
                return True
            elif not p or not q:
                return False
            return p.val == q.val

        stack = [(p, q)]
        while stack:            # while stack is not empty
            p, q = stack.pop()
            if not check(p, q):
                return False
            if p:
                stack.append((p.left, q.left))
                stack.append((p.right, q.right))

    def isSameTree_v3(self, p, q) -> bool:
        stack = [(p, q)]
        while stack:
            p, q = stack.pop()
            if not p and not q:
                continue
            if not p or not q:
                return False  
            if p.val == q.val:
                stack.append((p.left, q.left))
                stack.append((p.right, q.right))
            else:
                return False
        return True


    '''
    101. Symmetric Tree

    Given the root of a binary tree, check whether it is a mirror of itself
    (i.e., symmetric around its center).
    '''

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        stack = [(root.left, root.right)]
        while stack:
            l, r = stack.pop()
            if not l and not r:
                continue
            if not l or not r:
                return False
            if l.val != r.val:
                return False
            else:
                stack.append((l.left, r.right))
                stack.append((l.right, r.left))
        return True