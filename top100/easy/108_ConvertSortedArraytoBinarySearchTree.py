'''
108. Convert Sorted Array to Binary Search Tree

Given an integer array nums where the elements are sorted in ascending order,
convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree
in which the depth of the two subtrees of every node never differs by more than one.


[How to traverse tree]

1) Depth First Search (DFS) - adopt the depth as the priority,
so that one would start from a root and reach all the way down to certain leaf,
and then back to root to reach another branch.

The DFS strategy can further be distinguished as
preorder (root -> left -> right), inorder (left -> root -> right ), and postorder (left -> right -> root)
depending on the relative order among the root node, left node and right node.

2) Breadth First Search (BFS) - scan through the tree level by level,
following the order of height, from top to bottom
 The nodes on higher level would be visited before the ones with lower levels.

'''

# Definition for a binary tree node.
from stringprep import in_table_a1


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # inorder traversal of BST is an array sorted in ascending order
    # but its solution is not unique + hard to make height balanced tree
    # therefore, preorder (root -> left -> right) w/ always picking left middle node as a root

    # time complexity: O(n)
    # space complexity: O(logn) - recursion stack requires O(logn) because the tree is height-balanced
    #                   note that O(n) space used to store the output does not count as auxiliary space
    #                   so it's not included in the space complexity

    # always choose right middle node as a root
    def sortedArrayToBST_right(self, nums):
        if nums == []:
            return None
        idx = len(nums)//2
        # left -> root -> right
        head = TreeNode(nums[idx], None, None)
        head.left = self.sortedArrayToBST_right(nums[:idx])
        head.right = self.sortedArrayToBST_right(nums[idx+1:])
        return head

    # always choose left middle node as a root
    def sortedArrayToBST_left(self, nums):
        if nums == []:
            return None
        idx = len(nums)//2
        # bool(1): True, bool(0): False
        # if len(nums) == even
        if not len(nums)%2:
            idx -= 1
        head = TreeNode(nums[idx], None, None)
        head.left = self.sortedArrayToBST_left(nums[:idx])
        head.right = self.sortedArrayToBST_left(nums[idx+1:])
        return head

    # root -> left -> right
    def pre_order_traversal(self, node):
        elems = []
        if node:
            elems.append(node.val)
        # left
            elems += self.pre_order_traversal(node.left)
        # right
            elems += self.pre_order_traversal(node.right)
        return elems


if __name__ == '__main__':
    head_1 = Solution().sortedArrayToBST_right([1,2,3,4,5,6,7,8])
    '''
               5
          3        7
        2   4    6   8
       1            
    '''
    print(f"pre-order traverse (root -> left -> right)")
    print(Solution().pre_order_traversal(head_1)) # [5, 3, 2, 1, 4, 7, 6, 8]

    print("- - - - - - - - - - - - -")
    head_2 = Solution().sortedArrayToBST_left([1,2,3,4,5,6,7,8])
    '''
               4
          2        6
        1   3    5   7
                    8
    '''
    print(f"pre-order traverse (root -> left -> right)")
    print(Solution().pre_order_traversal(head_2)) # [4, 2, 1, 3, 6, 5, 7, 8]



            
