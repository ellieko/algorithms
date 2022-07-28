'''

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

'''

class Solution:
    # time complexity: O(n)
    # space complexity: O(n)
    def isValid_v1(self, s: str) -> bool:
        d = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for c in s:
            if c in d:
                stack.append(d[c])
            else:
                if len(stack) == 0 or c != stack.pop():
                    return False
        return len(stack) == 0

    # time complexity: O(n)
    # space complexity: O(n)
    def isValid_v2(self, s: str) -> bool:
        hash = {")":"(", "]":"[", "}":"{"}
        stack = []
        for char in s:
            if char in hash:
                if not stack or hash[char] != stack.pop():
                    return False
            else:
                stack.append(char)
        return stack == []

if __name__ == '__main__':
    print(Solution().isValid('(){}[]'))
    print(Solution().isValid('}'))