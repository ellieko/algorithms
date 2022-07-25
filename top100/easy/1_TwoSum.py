'''
1. Two Sum
https://leetcode.com/articles/two-sum/

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.

e.g.
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

---> Related Problems

167. Two Sum II - Input Array Is Sorted
https://leetcode.com/articles/two-sum-ii-input-array-is-sorted/

15. 3 Sum
https://leetcode.com/problems/3sum/

'''


class Solution:
    # Two Pass
    # time complexity: O(N)
    # space complexity: O(N)
    def twoSum_v1(self, nums, target):
        hash = {}
        for idx, num in enumerate(nums):
            hash[num] = idx
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in hash and idx != hash[complement]:
                return [idx, hash[complement]]

    # One Pass
    # time complexity: O(N)
    # space complexity: O(N)
    def twoSum_v2(self, nums, target):
        hash = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in hash:
                return [idx, hash[complement]]
            hash[num] = idx
        


    # what if it has multiple solutions
    # and want to bring out all of them but not duplicates

    # [3,3,0,6], 6) --> [[0,1], [2,3]]
    def twoSum_application(self, nums, target):
        hash = {}
        ans = []
        for idx,num in enumerate(nums):
            hash[num] = idx            
        for idx,num in enumerate(nums):
            complement = target - num
            if complement in hash and idx != hash[complement]:
                temp = {idx, hash[complement]}
                if temp not in ans:
                    ans.append(temp)
        return ans
    

if __name__ == '__main__':
    print(Solution().twoSum_v2([2,7,11,15], 9))                # [0,1]
    print(Solution().twoSum_v2([3,3,0,6], 6))                  # [0,1]

    print(Solution().twoSum_application([2,7,11,15], 9))
    print(Solution().twoSum_application([3,3,0,6], 6))