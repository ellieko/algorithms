'''
268. Missing Number

Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.

'''
class Solution:
    
    # use hashset
    # O(n) runtime complexity and O(n) extra space complexity
    def missingNumber(self, nums) -> int:
        d = set(nums)
        for val in range(len(nums)+1):
            if val not in d:
                return val
    
    # missing one element is a difference between the sum 0...N and the sum of a given list
    # sum of 0...N is gained with a formula (N)(N+1)//2
    # sum(list) -- time complexity: O(N)
    # O(n) runtime complexity and O(1) extra space complexity
    def missingNumber_v2(self, nums) -> int:
        expected_sum = len(nums)*(len(nums)+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

    # use bitwise XOR (exclusive or)
    # O(n) runtime complexity and O(1) extra space complexity
    def missingNumber_v3(self, nums) -> int:
        num = len(nums)
        for idx, elem in enumerate(nums):
            num ^= idx^elem
        return num

    # use sort
    # O(nlogn) runtime complexity and O(1) or O(n) extra space complexity
    # (depending on if it's allowed to modify the original list)
    def missingNumber_v4(self, nums) -> int:
        nums.sort()
        n = len(nums)
        if nums[0] != 0:
            return 0
        if nums[-1] != n:
            return n
        for i in range(1, n):
            if nums[i] != i:
                return i


if __name__ == '__main__':
    print(Solution().missingNumber_v4([3,0,1]))    # 2