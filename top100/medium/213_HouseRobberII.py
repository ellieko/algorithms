'''
213. House Robber II
https://leetcode.com/problems/house-robber-ii/

'''

from typing import List


class Solution:
    # time complexity: O(n)
    # space complexity: O(1)
    def rob(self, nums: List[int]) -> int:

        def helper(i, j) -> int:
            rob1, rob2 = 0, 0
            for k in range(i, j+1):
                temp = max(rob1 + nums[k], rob2)
                rob1, rob2 = rob2, temp
            return rob2

        return max(nums[0], helper(0, len(nums)-2), helper(1, len(nums)-1))