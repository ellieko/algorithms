'''
8. String to Integer (atoi)
https://leetcode.com/problems/string-to-integer-atoi/

Implement the myAtoi(string s) function,
which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'.
Read this character in if it is either.
This determines if the final result is negative or positive respectively.
Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached.
The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32).
If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.

0 <= s.length <= 200
s consists of English letters (lower-case and upper-case),
digits (0-9), ' ', '+', '-', and '.'.

'''

class Solution:
    # time complexity: O(n)
    # space complexity: O(1)
    def myAtoi(self, s: str) -> int:
        ans, idx, sign = 0,0,1
        s = s.strip()
        n = len(s)

        INT_MAX = pow(2,31)-1
        INT_MIN = -pow(2,31)

        if n > 1 and s[0] == '+':
            idx +=1
        elif n > 1 and s[0] == '-':
            sign = -1
            idx += 1

        while idx < n and s[idx].isdigit():
            digit = int(s[idx])

            # sign = 1
            # digit > 7 -> return INT_MAX (digit == 7: calculate as usual)
            # sign = -1
            # digit > 7 -> return INT_MIN (digit == 8: return INT_MIN)
            if ((ans > INT_MAX//10) or (ans == INT_MAX//10 and digit > INT_MAX % 10)):
                return INT_MAX if sign == 1 else INT_MIN

            ans = ans * 10 + digit
            idx += 1
        
        return sign * ans
