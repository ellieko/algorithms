'''
2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

'''

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return f"ListNode({self.val}, {self.next})"

class Solution:

    def addTwoNumbers(self, l1, l2):
        # time complexity: O(max(N, M))
        # space complexity: O(max(N, M))
        
        carry = 0
        dummy = ListNode(-1)
        node = dummy
        
        while l1 or l2 or carry:
            num = carry
            if l1:
                num += l1.val
                l1 = l1.next
            if l2:
                num += l2.val
                l2 = l2.next
    
            carry, val = divmod(num, 10)
            node.next = ListNode(val)
            node = node.next
            
        return dummy.next


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
    print(Solution().addTwoNumbers_v3(l1, l2))
