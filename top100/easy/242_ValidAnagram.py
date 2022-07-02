'''
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # from collections import Counter
        # return Counter(s) == Counter(t)
        
        return sorted(s) == sorted(t)
    
    # without using built-in functions
    # use only one dictionary
    def isAnagram_nobuiltin(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d = {}
        for c in s:
            d[c] = d[c] + 1 if c in d else 1
        for c in t:
            if c not in d:
                return False
            d[c] -= 1
        for c in d:
            if d[c] != 0:
                return False

        return True
    
if __name__ == '__main__':
    print(Solution().isAnagram_nobuiltin('anagram', 'anagram'))