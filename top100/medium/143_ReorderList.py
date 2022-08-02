'''
143. Reorder List
https://leetcode.com/problems/reorder-list/

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # time complexity: O(n)
    # space complexity: O(1)
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # identify the middle node - O(n)
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next
        slow.next = prev = None
        
        # reverse right-half portion - O(n/2)
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # merge two halfs - O(n/2)
        left, right = head, prev
        while right:
            tmp1, tmp2 = left.next, right.next
            left.next = right
            right.next = tmp1
            left, right = tmp1, tmp2