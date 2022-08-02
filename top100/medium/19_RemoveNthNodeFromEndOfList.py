'''
19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

e.g.
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

'''

# Definition for singly-linked list.
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
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        count = length - n
        dummy = ListNode(-1, head)
        prev = dummy
        while count != 0:
            prev = prev.next
            count -= 1
        
        prev.next = prev.next.next
    
        return dummy.next

    # One Pass - using two pointers
    def removeNthFromEnd_v2(self, head, n):
        dummy = ListNode(-1, head)
        l = r = dummy
        # advances first pointer first s.t. first and second pointer have n nodes gap
        for i in range(n+1):
            r = r.next
        # move first to the end, maintaining the gap
        while r:
            l, r = l.next, r.next
        l.next = l.next.next
        return dummy.next
        


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2, ListNode(3, ListNode(4, ListNode(5))))
    print(Solution().removeNthFromEnd_v2(head, 1))