'''

Given the head of a linked list, remove the nth node from the end of the list and return its head.

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
    # my first not pretty solution - use dummy node to resolve the first node!!
    def removeNthFromEnd(self, head, n):
        d, l = [], 0
        node = head
        while node:
            d.append(node)
            l += 1
            node = node.next
        if l - n == 0:
            head = head.next
            return head
        node, index = head, 1
        while index < l - n :
            node = node.next
            index += 1
        if node.next:
            node.next = node.next.next
        else:
            node.next = None
        return head

    # modified one, using "dummy node" (approach is the same)
    def removeNthFromEnd_v2(self, head, n):
        dummy = ListNode(0, head)
        node = head
        length = 0
        while node:
            length += 1
            node = node.next
        length -= n
        node = dummy
        while length > 0:
            length -= 1
            node = node.next
        node.next = node.next.next
        return dummy.next

    # another approach, using two pointers
    def removeNthFromEnd_v3(self, head, n):
        dummy = ListNode(0, head)
        first = second = dummy
        # advances first pointer first s.t. first and second pointer have n nodes gap
        for i in range(0, n+1):
            first = first.next
        # move first to the end, maintaining the gap
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2, ListNode(3, ListNode(4, ListNode(5))))
    print(Solution().removeNthFromEnd_v2(head, 1))