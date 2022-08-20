'''
19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

e.g.
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

'''

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Two Pass
    # time complexity: O(N)
    # space complexity: O(1)
    def removeNthFromEnd_v1(self, head, n):
        length = 0
        dummy = ListNode(0, head)
        
        # calculate the length
        curr, length = head, 0
        while curr:
            length += 1
            curr = curr.next
        
        # change n to be from the beginning of the list
        n = length - n
        
        # remove the node
        curr = dummy
        while curr and n > 0:
            curr = curr.next
            n -= 1
            
        # curr: the previous node of the node to remove
        curr.next = curr.next.next
    
        return dummy.next


    # One Pass - using two pointers
    # time complexity: O(N)
    # space complexity: O(1)
    def removeNthFromEnd_v2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        l = r = dummy

        # advance right pointer first for left and right pointers to have n nodes gap
        for _ in range(n):
            r = r.next
        
        # move right pointer to the tail, maintaining the gap
        # to find the previous node of the one to remove (l)
        while r.next:
            l = l.next
            r = r.next
        
        # remove the node (l.next)
        l.next = l.next.next
        
        return dummy.next
        


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2, ListNode(3, ListNode(4, ListNode(5))))
    print(Solution().removeNthFromEnd_v2(head, 1))