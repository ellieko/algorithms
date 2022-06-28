'''
171. Excel Sheet Column Number

Given a string columnTitle that represents the column title as appears in an Excel sheet,
return its corresponding column number.

'''

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        length = len(columnTitle)
        for i in range(length):
            ans += (26**(length-i-1))*(ord(columnTitle[i])-64)
        return ans

if __name__ == '__main__':
    print(Solution().titleToNumber("ZY"))   # 701