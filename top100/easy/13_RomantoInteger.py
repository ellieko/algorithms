# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

class Solution:
    def romanToInt(self, s: str) -> int:
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

    def romanToInt(self, s: str) -> int:
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
