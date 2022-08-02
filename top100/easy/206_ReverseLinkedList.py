'''
206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/

Given the head of a singly linked list,
reverse the list, and return the reversed list.

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        curr = head
        storage = []
        while curr:
            storage.append(curr.val)
            curr = curr.next
        if not storage:
            return
        head = ListNode(storage.pop())
        curr = head
        while curr and storage:
            curr.next = ListNode(storage.pop())
            curr = curr.next
        return head

    # time complexity: O(n)
    # space complexity: O(1)
    def reverseList_iter(self, head):
        prev = None
        curr = head
        while curr:
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next
        return prev

    # time complexity: O(n)
    # space complexity: O(n)
    def reverseList_recur(self, head):
        if (not head) or (not head.next):
            return head
        
        p = self.reverseList_recur(head.next)
        head.next.next = head
        head.next = None
        
        return p
         



if __name__ == '__main__':
    # 1 --> 2 --> 3 --> 4 --> 5 
    print()