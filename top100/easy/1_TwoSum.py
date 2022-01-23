'''

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.

e.g.
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

'''

class Solution:
    def twoSum(self, nums, target):
        hash = {}
        for idx, num in enumerate(nums):
            hash[num] = idx
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in hash and idx != hash[complement]:
                return [idx, hash[complement]]

if __name__ == '__main__':
    print(Solution().twoSum([2,7,11,15], 9))