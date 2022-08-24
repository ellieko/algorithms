'''
198. House Robber
https://leetcode.com/problems/house-robber/


'''

from typing import List


class Solution:
    # my approach
    # time complexity: O(n)
    # space complexity: O(n)
    # we are not reusing the previous values... so need to use extra space for list
    def rob(self, nums: List[int]) -> int:
        dp = [0, nums[0]]
        
        for i in range(2, len(nums)+1):
            dp.append(max(dp[i-1], dp[i-2] + nums[i-1]))
        
        return dp[len(nums)]

    # better
    # time complexity: O(n)
    # space complexity: O(1)
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2