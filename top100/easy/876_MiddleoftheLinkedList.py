'''
876. Middle of the Linked List

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

e.g.
Input: head = [1,2,3,4,5]
Output: [3,4,5]

e.g.
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # time complexity: O(n)
    # space complexity: O(n)
    def middleNode_v1(self, head):
        arr = [head]
        while arr[-1].next:
            arr.append(arr[-1].next)
        return arr[len(arr)//2]

    # two pointers
    # time complexity: O(n)
    # space complexity: O(1)
    def middleNode_v2(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
