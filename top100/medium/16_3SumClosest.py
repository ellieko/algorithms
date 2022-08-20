'''
16. 3Sum Closest
https://leetcode.com/problems/3sum-closest/

Given an integer array nums of length n and an integer target,
find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

'''

from typing import List


class Solution:
    # time complexity: O(n^2)
    # space complexity: O(n)
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])
        
        # fix the ith element
        for i in range(len(nums)-2):
            
            # j: leftmost pointer
            # k: rightmost pointer
            j, k = i+1, len(nums)-1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == target:
                    return target
                elif target > total:
                    j += 1
                    if j == k and k + 1 < len(nums):
                        k += 1
                else:
                    k -= 1
                if abs(total-target) < abs(res-target):
                    res = total
                    
        return res
            

if __name__ == '__main__':
    print(Solution().threeSumClosest([1,1,1,0], 100))