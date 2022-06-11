# 28. Implement strStr()

# find the index of the first occurrence of needle in haystack
# or -1 if needle is not part of haystack
# (edge case: if needle is empty string, return 0)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if len(needle) == 0:
        #     return 0
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

if __name__ == '__main__':
    print(Solution().strStr('hello', 'lo'))     # 3
    print(Solution().strStr('hello', ''))       # 0
    print(Solution().strStr('','hello'))        # -1