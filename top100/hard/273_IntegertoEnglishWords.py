'''
273. Integer to English Words
https://leetcode.com/problems/integer-to-english-words/

Convert a non-negative integer num to its English words representation.

'''

class Solution:
    # time complexity: O(n) (b.c. output is proportional to the number N of digits in the input)
    # space complexity: O(1)
    def numberToWords(self, num: int) -> str:
        res = []
        bigThrees = [(pow(10, 9), 'Billion'), (pow(10, 6), 'Million'),
                     (pow(10, 3), 'Thousand')]
        
        def readHundreds(n):
            numbers = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
                      'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen',
                      'Seventeen', 'Eighteen', 'Nineteen']
            tens = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty',
                    'Sixty', 'Seventy', 'Eighty', 'Ninety']
            if n//100:
                res.append(numbers[n//100])
                res.append('Hundred')
            if 0 <= n%100 < 20:
                res.append(numbers[n%100])
            elif n%100 >= 20:
                res.append(tens[n%100//10])
                res.append(numbers[n%10])
                    
                    
        for unit, eng in bigThrees:
            small, num = divmod(num, unit)
            if small:
                readHundreds(small)
                res.append(eng)
                
        readHundreds(num)
                
        res = " ".join(filter(lambda x: (x != ""), res)).strip()
        return res if res else "Zero"
            