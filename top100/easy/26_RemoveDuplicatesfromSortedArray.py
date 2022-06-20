'''
26. Remove Duplicates from Sorted Array
Given an integer array nums sorted in non-decreasing order,
remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same.

'''


class Solution:
    def removeDuplicates(self, nums) -> int:
        prev, i = nums[0], 1
        while i < len(nums):
            if nums[i] == prev:
                nums.pop(i)
                # here, index i needs to remain same
                # because now it has the next element
            else:
                prev = nums[i]
                i += 1
        return len(nums)


if __name__ == '__main__':
    print(Solution().removeDuplicates([1,1,2,2,3]))             # 3
    print(Solution().removeDuplicates([1,1]))                   # 1
    print(Solution().removeDuplicates([1,1,2,2,3,4,5]))         # 5
    print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))   # 5