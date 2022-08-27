'''
139. Word Break
https://leetcode.com/problems/word-break/

'''

from typing import List


class Solution:

    # bruteforce time complexity: O(n*n*m*n) ...?

    # time complexty: O(n * m * 20) = (length of s * length of dict * maximum length of word)
    # where n is the length of the input string, s, where m is the length of the wordDict
    # 1 <= n <= 300, 1 <= m <= 1000, and 20 is the max lenght of each word
    # space complexity: O(n)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False] * (len(s))
        dp.append(True)
        
        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
                    
        return dp[0]