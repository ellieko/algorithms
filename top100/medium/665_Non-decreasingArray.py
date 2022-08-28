'''
665. Non-decreasing Array
https://leetcode.com/problems/non-decreasing-array/

'''

from typing import List


class Solution:
    # time complexity: O(n)
    # space complexity: O(1)
    def checkPossibility(self, nums: List[int]) -> bool:
        changed = False
        for i in range(1, len(nums)):
            if nums[i-1] <= nums[i]:
                continue
            if changed:
                return False
                  
            # change left element
            # [4,2,3], [2,5,3]
            if i == 1 or nums[i-2] <= nums[i]:
                nums[i-1] = nums[i]
            
            # change right element
            # [3,4,2,3], [2,3,0]
            else:
                nums[i] = nums[i-1]
            changed = True
            
        return True