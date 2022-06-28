'''
202. Happy Number

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Input: n = 2
Output: false

'''

class Solution:
    def isHappy(self, n: int) -> bool:
        s, history = str(n), set()
        while s not in history:
            history.add(s)
            s = str(sum([int(i)**2 for i in s]))
            if s == '1':
                return True
        return False

    # Floyd's Cycle-Finding Algorithm
    # time complexity: O(logn)
    # space complexity: O(1)
    def isHappy_v2(self, n: int) -> bool:

        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit ** 2
            return total_sum
        
        slow_runner = n
        fast_runner = get_next(n)
        while fast_runner != 1 and slow_runner != fast_runner:
            slow_runner = get_next(slow_runner)
            fast_runner = get_next(get_next(fast_runner))
        return fast_runner == 1
        
if __name__ == '__main__':
   print(Solution().isHappy(19))
   print(Solution().isHappy(2))

   print(Solution().isHappy_v2(19))
   print(Solution().isHappy_v2(2))