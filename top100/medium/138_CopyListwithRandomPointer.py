'''
138. Copy List with Random Pointer
https://leetcode.com/problems/copy-list-with-random-pointer/

'''


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

from typing import Optional


class Solution:
    # time complexity: O(n)
    # space complexity: O(n)
    def copyRandomList_v1(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        dummy = Node(0)
        mapOldToNew = {}
        
        # deep copying its value and its next, creating mapToNewNodes
        oldCurr, newCurr = head, dummy
        while oldCurr:
            newCurr.next = Node(oldCurr.val)
            mapOldToNew[oldCurr] = newCurr.next
            oldCurr, newCurr = oldCurr.next, newCurr.next
            
        # deep copying its random pointer
        oldCurr, newCurr = head, dummy.next
        while oldCurr:
            if oldCurr.random:
                newCurr.random = mapOldToNew[oldCurr.random]
            oldCurr, newCurr = oldCurr.next, newCurr.next
        
        return dummy.next 

    # time complexity: O(n)
    # space complexity: O(n)
    def copyRandomList_v2(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapOldToCopy = {}

        curr = head
        while curr:
            copy = Node(curr.val)
            mapOldToCopy[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = mapOldToCopy[curr]
            copy.next = mapOldToCopy[curr.next]
            copy.random = mapOldToCopy[curr.random]
            curr = curr.next
        
        return mapOldToCopy[head]

    # time complexity: O(n)
    # space complexity: O(1)
    def copyRandomList_v3(self, head: 'Optional[Node]') -> 'Optional[Node]':
        return