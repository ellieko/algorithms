'''

Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

'''

class Solution:
    # brute force O(n^2) -- my implementation: Time Limit Exceeded
    def maxSubArray(self, nums):
        max_sum = nums[0]
        for i in range(len(nums)):
            curr_sum = 0
            for j in range(i, len(nums)):
                curr_sum += nums[j]
                max_sum = max(max_sum, curr_sum)
        return max_sum

    # Approach 2: Dynamic Programming, Kadane's Algorithm O(n)
    # whenever you see a question that asks for the maximum or minimum of something,
    # consider DP as a possibility
    def maxSubArray_v2(self, nums):
        curr_sum = max_sum = nums[0]
        for num in nums[1:]:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(curr_sum, max_sum)
        return max_sum

    # Approach 3: Divide and Conquer - less efficient more space O(nlogn)
    

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