'''
704. Binary Search

Given an array of integers nums which is sorted in ascending order,
and an integer target, write a function to search target in nums.
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Constraints:
1 <= nums.length <= 104
-10^4 < nums[i], target < 10^4
All the integers in nums are unique
nums is sorted in ascending order

'''

class Solution:
    # time complexity: O(logn)
    # space complexity: O(1)
    def iterative_binary(self, nums, target) -> int:
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid -1 
            else:
                low = mid + 1
        return -1

    # time complexity: O(logn)
    # space complexity: O(logn)
    def recursive_binary(self, nums, target) -> int:
        def recursive(low=0, end=len(nums)-1):
            if low > end:
                return -1
            mid = (low+end)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return recursive(mid+1, end)
            else:
                return recursive(low, mid-1)
        return recursive()

if __name__ == '__main__':
    print(Solution().iterative_binary([-1,0,3,5,9,12],13))
    print(Solution().recursive_binary([-1,0,3,5,9,12],13))
