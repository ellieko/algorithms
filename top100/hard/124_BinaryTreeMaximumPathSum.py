'''
124. Binary Tree Maximum Path Sum
https://leetcode.com/problems/binary-tree-maximum-path-sum/

'''

# Definition for a binary tree node
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:

    # time complexity는 O(n)
    # space complexity는 O(h)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        # initialize (the number of nodes in the tree >= 1)
        self.maxSum = root.val
        
        # the maximum sum up to the node w/o split
        def maxSumNoSplit(node):
            if not node:
                return 0
        	
            # because we can choose not to include the node to our path
            # if its max sum is less than zero
            left = max(0, maxSumNoSplit(node.left))
            right = max(0, maxSumNoSplit(node.right))
            
            # updates our self.maxSum
            # for the case when we choose to split at the node
            self.maxSum = max(self.maxSum, left + node.val + right)
            
            # the maximum sum up to the node w/o split
            return node.val + max(left, right)
                                  
        maxSumNoSplit(root)
        return self.maxSum