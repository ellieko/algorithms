'''
235. Lowest Common Ancestor of a Binary Search Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Given a binary search tree (BST),
find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes p and q
as the lowest node in T that has both p and q as descendants
(where we allow a node to be a descendant of itself).”
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Binary Search Tree (BST)
# the left subtree of a node contains only nodes with keys lesser than the node's key
# the right subtree of a node contains only nodes with keys greater than the node's key
# the left and right subtree each mush also be a binary search tree
class Solution:
    # time complexity: O(logn) (the height of tree because we're not visiting every node)
    # space complexity: O(1)
    def lowestCommonAncestor(self, root, p, q):
        cur = root
        
        while cur:
            if cur.val > p.val and cur.val > q.val:
                cur = cur.left
            elif cur.val < p.val and cur.val < q.val:
                cur = cur.right
            else:
                return cur
        