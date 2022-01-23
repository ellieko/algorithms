'''

Given an array of integers nums sorted in non-decreasing order,
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

e.g.
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

'''

class Solution:
    def searchRange(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                start = end = mid
                while start-1 >= 0 and nums[start-1] == target:
                    start -= 1
                while end+1 < len(nums) and nums[end+1] == target:
                    end += 1
                return [start, end]

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return [-1,-1]
    
if __name__ == '__main__':
    print(Solution().searchRange([5,7,7,8,8,10],8))
    print(Solution().searchRange([1],1))