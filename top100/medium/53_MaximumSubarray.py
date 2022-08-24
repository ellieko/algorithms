'''
53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

'''

from typing import List


class Solution:
    # time complexity: O(n)
    # space complexity: O(1)
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        maxSum = nums[0]
        
        for n in nums:
            if currSum < 0:
                currSum = 0 
            currSum += n
            if currSum > maxSum:
                maxSum = currSum
                
        return maxSum
    

if __name__ == '__main__':
    print(Solution().maxSubArray([1]))                      # should return 1 
    print(Solution().maxSubArray([1,-1,2,3,-1]))            # should return 5 
    print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # should return 6
    print(Solution().maxSubArray([5,4,-1,7,8]))             # should return 23
    print(Solution().maxSubArray([-2,1]))                   # should return 1

    print('- - - - - - - - - - -\n')

    print(Solution().maxSubArray_v2([1]))                      # should return 1 
    print(Solution().maxSubArray_v2([1,-1,2,3,-1]))            # should return 5 
    print(Solution().maxSubArray_v2([-2,1,-3,4,-1,2,1,-5,4]))  # should return 6
    print(Solution().maxSubArray_v2([5,4,-1,7,8]))             # should return 23
    print(Solution().maxSubArray_v2([-2,1]))                   # should return 1