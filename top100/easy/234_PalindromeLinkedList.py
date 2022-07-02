'''
234. Palindrome Linked List

Given the head of a singly linked list, return true if it is a palindrome.

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        if not ListNode:
            return None
        return f"ListNode({self.val, self.next}"

class Solution:
    # my first approach -> Time Limit Exceeded
    # takeaway: deep-copy 통해 "==" 를 새로 implement 하지 않는 이상
    # 같은 순서의 같은 val들을 가지고 있어도 다른 포인터면(?) 같지 않다고 나옴.
    # 똑같은 linked list 두 개를 만들었는데 같지 않다고 함
    # 그리고 엄청 길고 비효율적...
    def isPalindrome(self, head) -> bool:
        # find a length of a given linked list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # divide the list into halves (head and s2)
        curr = head
        if length % 2:                      # if a given length is odd
            for i in range(length//2):
                curr = curr.next
            s2 = ListNode(curr.val, curr.next)
            curr.next = None
        else:                               # if a given length is even
            for i in range(length//2-1):
                curr = curr.next
            s2 = curr.next
            curr.next = None

        # reverse the second half list, s2
        prev = None
        while s2:
            temp_next = s2.next
            s2.next = prev
            prev = s2
            s2 = temp_next

        # check if two list's elements are the same in the same order
        while prev and head:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True

    # make it list and check if the list is a palindrome
    # time complexity: O(n)
    # space complexity: O(n)
    def isPalindrom_iter(self, head) -> bool:
        storage = []
        curr = head
        while curr:
            storage.append(curr.val)
            curr = curr.next
        return storage == storage[::-1]

    # time complexity: O(n)
    # space complexity: O(n) for runtime stack because we are creating n stack frames
    # worse than the approach below because in many languages (such as Python), stack frames are large
    # and there's a maximum runtime stack depth of 1000
    # (you can increase it, but you risk causing memory errors with the underlying interpreter).
    # With every node creating a stack frame, this will greatly limit the maximum Linked List size the algorithm can handle.
    def isPalindrom_recur(self, head) -> bool:
        self.front_pointer = head

        def recursively_check(current_node=head):
            if current_node is not None:
                if not recursively_check(current_node.next):
                    return False
                if self.front_pointer.val != current_node.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True

        return recursively_check()


    # !!!!!!!BEST APPROACH!!!!!!!
    # Could you do it in O(n) time and O(1) space?
    # The only way we can avoid using O(n) extra space is by modifying the input in-place.
    # --> Reverse Second Half "In-place"
    def isPalindrome_v2(self, head) -> bool:
        if not head:
            return True
        
        first_half_end = first_half_end(head)
        second_half_start = reverse_list(first_half_end.next)

        def first_half_end(head):
            slow, fast = head, head
            while slow.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def reverse_list(position):
            prev = None
            while position:
                temp_next = position.next
                position.next = prev
                prev = position
                position = temp_next
            return prev
        
        p1 = head
        p2 = second_half_start

        while p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True


if __name__ == '__main__':
    # make a linked list [1,2,3,2,1]
    h1 = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))    # True
    h2 = ListNode(1, ListNode(2, ListNode(1)))                              # True
    h3 = ListNode(1, ListNode(2, ListNode(3)))                              # False
    print(Solution().isPalindrom_recur(h1))

            


