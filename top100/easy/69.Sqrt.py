'''
Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal digits are truncated,
and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator,
such as pow(x, 0.5) or x ** 0.5.

'''
class Solution:

    # first approach - not fast enough
    def mySqrt(self, x: int) -> int:
        for i in range(x+1):
            if i*i == x:
                return i
            if i*i > x:
                return i-1
        # return 0

if __name__ == '__main__':
    print(Solution().mySqrt(0))     # 0
    print(Solution().mySqrt(1))     # 1
    print(Solution().mySqrt(2))     # 1
    print(Solution().mySqrt(8))     # 2
    print(Solution().mySqrt(9))     # 3