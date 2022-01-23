'''

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
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

    # was better way to solve the problem (think more intended for this way)
    def addTwoNumbers_v2(self, l1, l2):
        pass

"""
def buildList(list):
    root = ListNode(list[0])
    node = root
    for i in range(1, len(list)):
        node.next = ListNode(list[i])
        node = node.next
    return root


if __name__ == '__main__':
    l1 = buildList([2, 4, 9])
    l2 = buildList([5, 6, 4, 9])
    s = Solution().addTwoNumbers(l1, l2)
"""
