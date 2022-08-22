'''
268. Missing Number

Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.

'''
class Solution:
    
    # 1) hashset
    # time complexity: O(n)
    # space complexity: O(n)
    def missingNumber(self, nums) -> int:
        d = set(nums)
        for val in range(len(nums)+1):
            if val not in d:
                return val
    
    # 2) expected sum
    # missing one element is a difference between the sum 0...N and the sum of a given list
    # sum of 0...N is gained with a formula (N)(N+1)//2
    # time complexity: O(N) - sum(nums) 
    # space complexity: O(1)
    def missingNumber_v2(self, nums) -> int:
        expected_sum = len(nums)*(len(nums)+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

    # use bitwise XOR (exclusive or)
    # time complexity: O(n)
    # space complexity: O(1)
    def missingNumber_v3(self, nums) -> int:
        num = len(nums)
        for idx, elem in enumerate(nums):
            num ^= idx^elem
        return num

    # sort
    # time complexity: O(nlogn)
    # space complexity: O(n)
    def missingNumber_v4(self, nums) -> int:
        nums.sort()
        val = 0
        for n in nums:
            if val != n:
                return val
            val +=1
        return val


if __name__ == '__main__':
    print(Solution().missingNumber_v4([3,0,1]))    # 2