'''
424. Longest Repeating Character Replacement
https://leetcode.com/problems/longest-repeating-character-replacement/

You are given a string s and an integer k.
You can choose any character of the string and change it to any other uppercase English character.
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get
after performing the above operations.

e.g. ABAB, 2 ---> 4

'''

class Solution:

    # sliding window
    # time complexity: O(26n)       ---> can optimize to O(n)
    # space compexity: O(26n)
    def characterReplacement_v1(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r-l+1)

        return res

    # time complexity: O(n)
    # space compexity: O(26n)
    def characterReplacement_v2(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0    # max frequency
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r-l+1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r-l+1)

        return res