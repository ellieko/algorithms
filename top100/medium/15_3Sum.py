'''

Given an integer array nums,
return all the triplets [nums[i], nums[j], nums[k]] such that
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

e.g.
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

'''

# nums_type: List[int]) -> return_type: List[List[int]]
class Solution:

    # return type is set of tuples...
    def threeSum(self, nums):
        nums.sort()
        ans = set()
        l = len(nums)
        for idx, num in enumerate(nums):
            lo, hi = idx+1, l-1
            while lo < hi:
                if (nums[lo] + nums[hi]) < -num:
                    lo += 1
                elif (nums[lo] + nums[hi] > -num):
                    hi -= 1
                else:
                    ans.add((nums[idx], nums[lo], nums[hi]))
                    lo += 1
        return ans

if __name__ == '__main__':
    print(Solution().threeSum([-1,0,1,2,-1,-4]))
    print(Solution().threeSum([0,0,0,0]))           # should return [[0,0,0]]
    print(Solution().threeSum([-2,0,1,1,2]))        # should return [[-2,0,2],[-2,1,1]]