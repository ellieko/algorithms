'''
977. Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.

'''

class Solution:
    # time complexity: O(n)
    # space complexity: O(n)
    def sortedSquares(self, nums):
        n = len(nums)
        left, right = 0, n-1
        ans = [0]*n
        for i in range(n-1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                ans[i] = nums[right]**2
                right -= 1
            else:
                ans[i] = nums[left]**2
                left += 1
        return ans



if __name__ == '__main__':
    print(Solution().sortedSquares([-4,-1,0,3,10]))

