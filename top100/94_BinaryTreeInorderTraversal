'''

Given the root of a binary tree, return the inorder traversal of its nodes' values.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # recursive way
    # Time complexity: O(n)
    # because the recursive function is T(n) = 2 T(n/2) + 1
    def inorderTraversal(self, root):
        ans, node = [], root
        if not node:
            return []
        if node.left:
            ans.extend(self.inorderTraversal(node.left))
        ans.append(node.val)
        if node.right:
            ans.extend(self.inorderTraversal(node.right))
        return ans

    # iterative way -- using stack!
    # Time complexity: O(n)
    def inorderTraversal_v2(self, root):
        ans, stack = [], []
        curr = root

        # needs to stop when curr is None and stack is also empty
        while curr != None or stack != []:
            while curr != None:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            ans.append(curr.val)
            # if curr doesnt have right node, it will pop the parent node from the stack
            curr = curr.right
        return ans

    # using Morris traversal