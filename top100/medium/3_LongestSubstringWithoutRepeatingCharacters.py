'''
Given a string s, find the length of the longest substring without repeating characters.

e.g.
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''


class Solution:

    # Runtime: 2851 ms (time complexitiy: O(n^2))
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        if len(s) <= 1:
            return len(s)
        for i in range(len(s)-1):
            l = 1
            storage = [s[i]]
            for j in range(i+1, len(s)):
                elem = s[j]
                if elem in storage:
                    break
                else:
                    l += 1
                    storage.append(elem)
            if l > maxlen:
                maxlen = l
        return maxlen

    # Runtime: 99 ms (time complexity: O(n))
    def lengthOfLongestSubstring_v2(self, s: str) -> int:
        chars = [None] * 128
        left = right = 0
        res = 0
        while right < len(s):
            r = s[right]
            index = chars[ord(r)]
            if index != None and index >= left and index < right:
                left = index + 1
            res = max(res, right - left + 1)
            chars[ord(r)] = right
            right += 1
        return res

if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring('abcadbc'))
    print(Solution().lengthOfLongestSubstring_v2('abcadbc'))

    print(Solution().lengthOfLongestSubstring('abcabca'))
    print(Solution().lengthOfLongestSubstring_v2('abcabca'))

    print(Solution().lengthOfLongestSubstring('abcbbca'))
    print(Solution().lengthOfLongestSubstring_v2('abcbbca'))