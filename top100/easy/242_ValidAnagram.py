'''
242. Valid Anagram
https://leetcode.com/problems/valid-anagram/submissions/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

'''

class Solution:
    # time complexity: O(nlogn)
    # space complexity: O(n)
    def isAnagram_v1(self, s: str, t: str) -> bool:
        # from collections import Counter
        # return Counter(s) == Counter(t)
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
    
    # without using built-in functions
    # use only one dictionary
    # time complexity: O(n+m)
    # space complexity: O(n)
    def isAnagram_v2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        d = {}
        for c in s:
            d[c] = 1 + d.get(c, 0)
        
        for c in t:
            if c not in d:
                return False
            d[c] = d[c] - 1
            if d[c] == 0:
                del d[c]
        
        return True
    
if __name__ == '__main__':
    print(Solution().isAnagram_nobuiltin('anagram', 'anagram'))