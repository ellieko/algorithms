'''
238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums,
return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

'''

class Solution:
    # time complexity: O(n)
    # space complexity: O(1)
    def productExceptSelf(self, nums):
        res = [1] * len(nums)
        prefix = postfix =  1

        # prefix
        for i in range(len(nums)):
            res[i] = prefix
            prefix = prefix * nums[i]
        
        # postfix
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * postfix
            postfix = postfix * nums[i]

        return res