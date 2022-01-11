'''

Given a sorted array of distinct integers and a target value, 
return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

'''

class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1
        mid_index = -1  # hasn't been defined yet
        while left <= right:
            # mid_index = (left + right) >> 1
            mid_index = (left + right) // 2
            mid_number = nums[mid_index]
            if target == mid_number:
                return mid_index
            elif target < mid_number:
                right = mid_index - 1
            else:
                left = mid_index + 1
        #if mid_number < target: return mid_index + 1
        #if mid_number > target: return mid_index 
        return left

if __name__ == '__main__':
    print(Solution().searchInsert([1,3,5,6], 5)) # should return 2 (found)
    print(Solution().searchInsert([1,3,5,6], 2)) # should return 1 (not found)
    print(Solution().searchInsert([1,3,5,6], 7)) # should return 4 (not found)

    print(Solution().searchInsert([1,3,5,6,9], 5)) # should return 2 (found)
    print(Solution().searchInsert([1,3,5,6,9], 2)) # should return 1 (not found)
    print(Solution().searchInsert([1,3,5,6,9], 7)) # should return 4 (not found)
    print(Solution().searchInsert([1,3,5,6,9], 11)) # should return 5 (not found)