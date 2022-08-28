'''
33. Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function,
nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
such that the resulting array is
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

e.g.
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

e.g.
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

'''

class Solution:
    def search(self, nums, target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            
            # non-rotated from the index l to mid
            elif nums[l] <= nums[mid]:
                if nums[mid] < target:
                    l = mid + 1
                else:   # two possibilities
                    if nums[l] > target:
                        l = mid + 1
                    else:
                        r = mid -1

            # rotated (rotation index is between l and mid)
            else:
                if nums[mid] > target:
                    r = mid - 1
                else:   # two possibilities
                    if nums[r] < target:
                        r = mid - 1
                    else:
                        l = mid + 1

        return -1


    # time complexity: O(logn)
    # space complexity: O(1)
    def search(self, nums, target: int) -> int:
        lo, hi = 0, len(nums)-1
        
        while lo <= hi:
            mid = (lo+hi)//2
            if nums[mid] == target:
                return mid
            
            # left-sorted portion
            # if target is smaller than nums[mid]
            # it can be even smaller than nums[left] or not
            elif nums[lo] <= nums[mid]:     # ascending   
                if target < nums[lo] or target > nums[mid]:
                    lo = mid + 1
                else: # when the target is smaller than nums[mid] but than nums[0]
                    hi = mid - 1
                    
            # right-sorted portion
            # if target is greater than nums[mid]
            # it can be even greater than the last indexed element or not
            else:
                if target > nums[hi] or target < nums[mid]:
                    hi = mid - 1
                else: # when it's greater than nums[mid] but less than nums[-1]
                    lo = mid + 1
        return -1

    
    def search_v1(self, nums, target):
        '''
        two binary search
        one for finding a pivot index and the another for searching target

        elem = nums[0]
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] < elem:
                r = mid - 1
            elif nums[mid] > elem:
                l = mid + 1
            else:
                break

        # mid: pivot index
        if target > elem:
            l, r = 0, mid
        else:
            l, r = mid + 1, len(nums) - 1

        while l <= r:
            mid = (l+r)//2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return -1
        '''

    def search_v2(self, nums, target):
        
        idx = 0 
        while idx < len(nums)-1 and nums[idx] < nums[idx+1]:
            idx += 1
        return self.binarySearch(nums, target, idx, 0, len(nums) - 1)
        
    def binarySearch(self, nums, target, pivot, left, right):
        if pivot + 1 == len(nums) or pivot == -1:
            while left <= right:
                mid = (left+right)//2
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        else:
            mid = pivot
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return -1
            else:
                return max(self.binarySearch(nums, target, -1, left, mid-1), self.binarySearch(nums, target, -1, mid+1, right))
        return -1


    # solution 1.
    # find rotation_index and if nums[0] < target: search(rotation_index, len(nums)-1)
    #                         else:                search(0, rotation_index)

    def search_v3(self, nums, target):
        def find_rotation_index(left, right):
            if nums[left] < nums[right]:
                return 0
            while left <= right:
                pivot = (left+right)//2
                if nums[pivot] > nums[pivot + 1]:
                    return pivot + 1
                else:
                    if nums[pivot] < nums[left]:
                        right = pivot - 1
                    else:
                        left = pivot + 1
        def binary_search(left, right):
            while left <= right:
                pivot = (left+right)//2
                if nums[pivot] == target:
                    return pivot
                else:
                    if nums[pivot] < target:
                        left = pivot + 1
                    else:
                        right = right - 1
            return -1
        n = len(nums)
        if n == 1: return 0 if nums[0] == target else -1
        rotate_index = find_rotation_index(0, n-1)
        # if the target is the smallest element
        if nums[rotate_index] == target:
            return rotate_index
        # if the array is not rotated
        if rotate_index == 0:
            return binary_search(0, n-1)
        if target < nums[0]:
            return binary_search(rotate_index+1, n-1)
        return binary_search(0, rotate_index-1)




if __name__ == '__main__':
    '''
    print(f"nums: [4,5,6,7,0,1,2] target: 0 --> ans: {Solution().search([4,5,6,7,0,1,2], 0)}")
    print(f"nums: [4,5,6,7,0,1,2] target: 3 --> ans: {Solution().search([4,5,6,7,0,1,2], 3)}")
    print(f"nums: [1] target: 1             --> ans: {Solution().search([1], 1)}")
    print(f"nums: [1,3] target: 1           --> ans: {Solution().search([1, 3], 1)}")
    print(f"nums: [3,1] target:3            --> ans: {Solution().search([3, 1], 3)}")
    '''

    print(Solution().search_v2([1,3],3))