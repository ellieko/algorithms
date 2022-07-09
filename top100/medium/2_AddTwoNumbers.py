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
    def __repr__(self):
        return f"ListNode({self.val}, {self.next})"

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

    # Jul 6, 2022
    # time complexity: O(max(N,M)+logK)
    # space complexity: O(K) where K is the length of the sum

    def addTwoNumbers_v2(self, l1, l2):
        num = 0
        amount = 1
        while l1 or l2:
            if l1:
                num += l1.val * amount
                l1 = l1.next
            if l2:
                num += l2.val * amount
                l2 = l2.next
            amount *= 10
            
        if num == 0:
            head = ListNode(0)
        else:
            head = ListNode(num%10)
            num //= 10
            curr = head
        while num > 0:
            num, rmd = divmod(num, 10)
            curr.next = ListNode(rmd)
            curr = curr.next
            
        return head

    # having dummy head and return dummy head's next is better
    # time complexity: O(max(n,m))
    # space complexity: O(max(n,m))
    def addTwoNumbers_v3(self, l1, l2):
        dummy_head = ListNode(-1)
        curr = dummy_head
        carry = 0
        while l1 or l2 or carry != 0:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            carry, out = divmod(carry + l1_val + l2_val, 10)
            curr.next = ListNode(out)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next
        return dummy_head.next

            


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
