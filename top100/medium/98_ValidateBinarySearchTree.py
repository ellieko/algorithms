'''
98. Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

binary search tree -> all left side nodes need to be less than the root's node value
                      all right side nodes need to be greater than the root's node value
                      (therefore there min and max value changes every time)

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    # approach 1) Top-down DFS low and high (valid interval)
    # time complexity: O(N) since we visit each node exactly once
    # space complexity: O(N) since we keep up to the entire tree (recursion stack)

    def isValidBST_v1(self, root) -> bool:
        return self.validate(root, None, None)
    
    def validate(self, node, low, high):
        if not node:
            return True
        if low != None and low >= node.val:
            return False
        if high != None and node.val >= high:
            return False
        return self.validate(node.left, low, node.val) and self.validate(node.right, node.val, high)


    # approach 2) Inorder Traversal (94. Binary Tree Inorder Traversal)
    # when we do inorder traversal, to satisfy binary search tree, previous elem has to be always smaller
    # time complexity: O(N) since we visit each node exactly once
    # space complexity: O(N) since we keep up to the entire tree (recursion stack)

    def isValidBST_v2(self, root) -> bool:
        prev, curr = None, root
        stack = []
        while curr or len(stack) != 0:

            while curr:
                stack.append(curr)
                curr = curr.left

            # curr == None
            curr = stack.pop()
            if prev != None and prev >= curr.val:
                return False
            prev = curr.val
            curr = curr.right
        return True



    