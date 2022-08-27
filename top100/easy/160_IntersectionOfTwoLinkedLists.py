'''
160. Intersection of Two Linked Lists

Given the heads of two singly linked-lists headA and headB,
return the node at which the two lists intersect.
If the two linked lists have no intersection at all, return null.

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # approach 1) time complexity: O(N+M)
    #             space complexity: O(N)
    # using hash is much faster in looking for an element
    # use set() is the key
    def getIntersectionNode(self, headA, headB):
        storage = set()
        curr = headA
        while curr:
            storage.add(curr)
            curr = curr.next
        curr = headB
        while curr:
            if curr in storage:
                return curr
            curr = curr.next

    # approach 2) time complexity: O(N+M)
    #             space complexity: O(1)
    # using the difference of length of two list is the key to solve the problem
    # if they have same length, no problem to move on to next elem and compare
    # we can make them to not have difference of length
    def getIntersectionNode_v2(self, headA, headB):
        p1, p2 = headA, headB
        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1
    
