'''
83. Remove Duplicates from Sorted List

Given the head of a sorted linked list,
delete all duplicates such that each element appears only once.
Return the linked list sorted as well.

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def __repr__(self):
        curr = self.head
        repr = ''
        while curr:
            if curr != self.head:
                repr += ' --> '
            repr += f"{curr.val}"
            curr = curr.next
        return f"[{repr}]"
    

    # given problem to implement
    def deleteDuplicates(self):
        curr = self.head
        while curr and curr.next:               # while curr and curr.next both are not None
            if curr.val == curr.next.val:
                curr.next = curr.next.next      # now it got new curr.next (so shouldn't move on to next elem)
            else:
                # move on to next elem only when they weren't same
                curr = curr.next
        return self.head

if __name__ == '__main__':
    # test linkedlist class
    temp_list = LinkedList(ListNode(1))
    temp_list.head.next = ListNode(1)
    temp_list.head.next.next = ListNode(1)
    print(temp_list)

    # test deleteDuplicates
    temp_list.deleteDuplicates()
    print(temp_list)