'''
25. Reverse Nodes in k-Group
https://leetcode.com/problems/reverse-nodes-in-k-group/

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

'''

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # time complexity: O(n)
    # space complexity: O(1)
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        while True:
            kth = self.getKthNode(groupPrev, k)
            if not kth: break
            groupNext = kth.next

            # reverse group
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev, curr = curr, temp

            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp

        return dummy.next

    def getKthNode(self, node, k):
        while node and k > 0:
            node = node.next
            k -= 1
        return node
