'''
105. Construct Binary Tree from Preorder and Inorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Given two integer arrays preorder and inorder
where preorder is the preorder traversal of a binary tree and
inorder is the inorder traversal of the same tree, construct and return the binary tree.

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # time complexity: O(n)
    # space complexity: O(n)
    def buildTree(self, preorder, inorder):
        # pre-order: root -> left -> right
        # the first element is always root
        # can give us the information of root node
        
        # in-order: left -> root -> right
        # until the root node, everything is left subtree
        # after the root node, everything is right subtree
        # can give us the length of each subtree

        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0]) # mid itself is a length of left subtree
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return root
        