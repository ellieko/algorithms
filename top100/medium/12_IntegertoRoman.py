'''
12. Integer to Roman
https://leetcode.com/problems/integer-to-roman/

e.g. num = 3            ->  "III"
     (b.c. 3 is represented as 3 ones)
'''

class Solution:
    # time complexity: O(1)
    # space complexity: O(1)
    def intToRoman_v1(self, num: int) -> str:
        thousands = ["", "M", "MM", "MMM"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return (thousands[num//1000] + hundreds[num%1000//100] +
                tens[num%100//10] + ones[num%10])

    def intToRoman_v2(self, num: int) -> str:
        digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), 
                  (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), 
                  (5, "V"), (4, "IV"), (1, "I")]
        
        res = ""
        for val, roman in digits:
            if num == 0: break
            count, num = divmod(num, val)
            res += roman * count
        return res