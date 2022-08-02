'''
141. Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list
that can be reached again by continuously following the next pointer.
Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
Note that pos is not passed as a parameter. (so it's for test, not for us to use)

Return true if there is a cycle in the linked list. Otherwise, return false.

e.g.
Input: head = [3,2,0,-4], pos = 1
Output: true

'''


# Definition for singly-linked list.

class ListNode:
    def __init__(self, x, n = None):
        self.val = x
        self.next = n
    def __repr__(self):
        return f"ListNode({self.val})"

class Solution:
    # approach 1) simply check if node is already in list
    # time and space complexity: O(n)
    def hasCycle(self, head) -> bool:
        history = set()
        while head:
            if head in history:
                return True
            history.add(head)
            head = head.next
        return False

    # approcah 2) slow and fast (Floyd's Cycle Finding Algorithm)
    # time complexity: O(n), space complexity: O(1)
    # if slow and fast (pointers) meet each other again --> cycle
    # else fast will hit null --> no cycle
    def hasCycle_v2(self, head) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next        # possible because we check fast != null
            fast = fast.next.next   # possible because we check fast.next != null
            if slow == fast:
                return True
        return False

if __name__ == '__main__':
    h = ListNode(3, ListNode(2, ListNode(0, ListNode(4))))
    h.next.next.next.next = h.next
    head = h
    for i in range(7):
        print(h, end=" ")
        h = h.next
    print()

    print(Solution().hasCycle(head))
    print(Solution().hasCycle_v2(head))