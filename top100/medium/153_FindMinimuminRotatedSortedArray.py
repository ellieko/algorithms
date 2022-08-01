'''
153. Find Minimum in Rotated Sorted Array
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

'''

class Solution:
    # time complexity: O(logn)
    # space complexity: O(1)
    def findMin_v1(self, nums) -> int:
        l, r = 0, len(nums) - 1
        m = nums[0]
        
        while l <= r:
            # if array is sorted
            if nums[l] <= nums[r]:
                m = min(m, nums[l])
                break

            # binary search
            else:
                mid = (l+r)//2
                if nums[l] <= nums[mid]:
                    l = mid + 1
                else:   # nums[l] > nums[mid]
                    m = min(m, nums[mid])
                    l, r = l + 1, mid - 1
        return m


    # my inital approach
    # time complexity: O(logn)
    # space complexity: O(1)
    def findMin_v2(self, nums) -> int:
        l, r = 0, len(nums) - 1
        m = None
        
        while l <= r:
            if nums[l] <= nums[r]:
                return nums[l]
            else:   # nums[l] > nums[r]
                mid = (l+r)//2
                if nums[l] <= nums[mid]:    # increasing part
                    l = mid + 1
                else:   # nums[l] > nums[mid]
                    l = l + 1
                    r = mid