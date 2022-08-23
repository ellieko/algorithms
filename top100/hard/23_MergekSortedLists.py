'''
23. Merge k Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

'''

# Definition for singly-linked list.
from typing import List,Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # 1) bruteforce approach
    # time complexity: O(nlogn) where n is the total number of nodes
    # space complexity: O(1)
    def mergeKLists_v1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # save all values into the list, and sort, convert it to linked list
        values = []
        for l in lists:
            curr = l
            while curr:
                values.append(curr.val)
                curr = curr.next
        values.sort()
        
        dummy = ListNode()
        curr = dummy
        for i in range(len(values)):
            curr.next = ListNode(values[i])
            curr = curr.next
            
        return dummy.next


    # time complexity: O(nlogk) where n is the average length of two linked list to be merged and k is the length of lists
    # space complexity: O(n*k)
    def mergeKLists_v2(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1, l2 = lists[i], lists[i+1]
                merged = self.mergeTwoLists(l1, l2)
                mergedLists.append(merged)
            lists = mergedLists
        
        return lists[0]

        
    # time complexity: O(n) where n is the total number of two given linked lists
    # space complexity: O(1)
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        tail.next = l1 if l1 else l2

        return dummy.next
