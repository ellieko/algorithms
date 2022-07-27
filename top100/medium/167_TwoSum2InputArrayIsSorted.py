'''
167. Two Sum II - Input Array Is Sorted
'''

class Solution:
    # brute force - time limit exceeded
    def twoSum(self, numbers, target: int):
        for i in range(len(numbers)-1):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]

    # time complexity: O(n)
    # space complexity: O(1)
    def twoSum_v2(self, numbers, target: int):
        left, right = 0, len(numbers)-1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left+1, right+1]
            elif total > target:
                right -= 1
            else:
                left += 1
        return [-1,-1]