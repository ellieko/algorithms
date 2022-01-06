# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2, s1, s2 = l1, l2, "", ""
        while n1:
            s1 += str(n1.val)
            n1 = n1.next
        while n2:
            s2 += str(n2.val)
            n2 = n2.next
        num = int(s1) + int(s2)
        s = str(num)
        node = ListNode(s[-1])
        root = node
        i = len(s) - 2
        while i >= 0:
            node.next = ListNode(s[i])
            node = node.next
            i -= 1
        return root
