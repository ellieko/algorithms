'''
13. Roman to Integer
https://leetcode.com/problems/roman-to-integer/

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

e.g. s = "III"          ->  3
     (b.c. III = 3)

e.g. s = "MCMXCIV"      ->  1994
     (b.c. M = 1000, CM = 900, XC = 90 and IV = 4)

'''

class Solution:
    # time complexity: O(1)
    # space complexity: O(1)
    def romanToInt_v1(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
             'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        i, num = 0, 0
        while i < len(s):
            if i+1 < len(s) and s[i:i+2] in d:
                num += d[s[i:i+2]]
                i += 2
            else:
                num += d[s[i]]
                i += 1
        return num

    # time complexity: O(1)
    # space complexity: O(1)
    # the given input should be consiting of the letters that are continuously increasing in general
    # but if they don't, that means they are like 40, 90,
    # so we need to subtract the current position's value from the next position's value
    # then we don't have to have 40, 90's Roman in our dictionary
    def romanToInt_v2(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        i, num = 0, 0
        while i < len(s):
            if i + 1 < len(s) and d[s[i]] < d[s[i + 1]]:
                num += d[s[i+1]] - d[s[i]]
                i += 2
            else:
                num += d[s[i]]
                i += 1
        return num
