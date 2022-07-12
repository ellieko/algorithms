'''
12. Integer to Roman
https://leetcode.com/problems/integer-to-roman/

'''

class Solution:
    def intToRoman(self, num: int) -> str:
        # 1 <= num <= 3999
        
        # num // 1000: 0, 1, 2, 3
        # 0, 1000, 2000, 3000
        thousands = ["", "M", "MM", "MMM"]
        
        # num // 100: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
        # 0, 100, 200, 300, 400, 500, 600, 700, 800, 900
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        
        # num // 10: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
        # 0, 10, 20, 30, 40, 50, 60, 70, 80, 90
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        
        # num // 1: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        
        return thousands[num//1000] + hundreds[num%1000//100] + tens[num%100//10] + ones[num%10]


if __name__ == '__main__':
    print(Solution().intToRoman(58))