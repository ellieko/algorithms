'''

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

'''

class Solution:
    def isValid(self, s: str) -> bool:
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