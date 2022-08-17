'''
387. First Unique Character in a String
https://leetcode.com/problems/first-unique-character-in-a-string/

Given a string s, find the first non-repeating character in it and return its index.
If it does not exist, return -1.

1 <= s.length <= 105
s consists of only lowercase English letters
'''

class Solution:
    # time complexity: O(n+n) -> O(n)
    # space complexity: !!!!! O(1) because English alphabet contains 26 letters !!!!!
    def firstUniqChar_v1(self, s: str) -> int:
        d = {}
        for c in s:
            d[c] = d[c] + 1 if c in d else 1
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1


if __name__ == '__main__':
    print(Solution().firstUniqChar_v2("loveleetcode"))  # 2

