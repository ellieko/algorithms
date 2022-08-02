'''
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list.
The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # my implementation: way too long - Runtime: 36 ms
    def mergeTwoLists(self, list1, list2):
        n1, n2, root = list1, list2, None
        if not n1 and not n2:
            root = None
        elif n1 and not n2:
            root = n1
        elif n2 and not n1:
            root = n2
        else:
            if n1.val <= n2.val:
                root = ListNode(n1.val)
                n1 = n1.next
            else:
                root = ListNode(n2.val)
                n2 = n2.next
            node = root
            while n1 or n2:
                if n1 and n2:
                    if n1.val <= n2.val:
                        node.next = ListNode(n1.val)
                        n1 = n1.next
                    else:
                        node.next = ListNode(n2.val)
                        n2 = n2.next
                elif n1 and not n2:
                    node.next = n1
                    n1 = None
                else:
                    node.next = n2
                    n2 = None
                node = node.next
        return root

    # recursive way - Runtime: 46 ms
    def mergeTwoLists_v2(self, list1, list2):
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val <= list2.val:
            list1.next = self.mergeTwoLists_v2(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists_v2(list1, list2.next)
            return list2

    # iterative way - Runtime: 36 ms
    # runtime complexity: O(N+M)
    # space complexity: O(1)
    def mergeTwoLists_v3(self, list1, list2):
        prehead = ListNode(-1)
        prev = prehead
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next
        
        prev.next = list1 if list1 else list2
        return prehead.next

def buildList(list):
    root = ListNode(list[0])
    node = root
    for i in range(1, len(list)):
        node.next = ListNode(list[i])
        node = node.next
    return root

if __name__ == '__main__':
    l1= buildList([1,2,4])
    l2 = buildList([1,3,4])
    s = Solution().mergeTwoLists(l1,l2)

    print(ListNode(-1))