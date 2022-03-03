'''
Given an integer array nums,
return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an arry
by deleting some or no elements w/o changing the order of the remaining elements.
For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,7].

e.g. lengthOfLIS([])
'''

def lengthOfLIS(nums):
    dp = [1 for i in range(len(nums))]
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

if __name__ == '__main__':
    print(lengthOfLIS([10,9,2,5,3,7,101,18]))       # 4