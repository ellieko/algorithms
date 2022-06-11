'''

Given an integer array nums and an integer val,
remove all occurrences of val in nums in-place.
The relative order of the elements may be changed.

'''


class Solution:

    # my approach
    def removeElement(self, nums, val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)
    
    # using two pointers
    # only cares about until ith element
    def removeElement_v2(self, nums, val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        print(nums)
        return i

    # reduce length of array
    def removeElement_v3(self, nums, val: int) -> int:
        n = len(nums)
        i = 0 
        while i < n:
            if nums[i] == val:
                nums.pop(i)
                n -= 1
            else:
                i += 1
        return n
    
if __name__ == '__main__':
    print(Solution().removeElement_v2([2,2,2,3,1,6,2], 2))      # 3
    print(Solution().removeElement_v3([2,2,2,3,1,6,2], 2))      # 3
    