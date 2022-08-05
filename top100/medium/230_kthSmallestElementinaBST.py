'''
230. kth Smallest Element in a BST
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Given the root of a binary search tree, and an integer k,
return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    # iterative way
    def kthSmallest_v1(self, root, k: int) -> int:
        # DFS in-order traversal -> sorted list

        # time compelxity: O(H + k) where H is a tree height
        # it is defined by the stack, which contains at least H + k elements,
        # since before starting to pop out one has to go down to a leaf
        # This results in O(log N + k) for the balanced tree and
        #      O(N + k) for completely unbalanced tree with all the nodes in the left subtree

        # space complexity: O(H) to keep the stack, where H is a tree height
        # it makes O(N) in the worst case of the skewed tree, and O(logN) in the average case of the balanced tree
    
        cur, stack = root, []
        
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            k -= 1
            if k == 0:
                return cur.val
            cur = cur.right

    # recursive way
    # time complexity: O(N) to build a traversal
    # space complexity : O(N) to keep an inorder traversal
    def kthSmallest_v2(self, root, k: int) -> int:
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        return inorder(root)[k-1]

            