'''

Implement next permutation,
which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is impossible,
it must rearrange it to the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

e.g.
Input: nums = [1,2,3]
Output: [1,3,2]

e.g.
Input: nums = [3,2,1]
Output: [1,2,3]

[1, 2] -> [2, 1]
[1, 2, 3] -> [1, 3, 2]
[2, 1, 3] -> [2, 3, 1]
[3, 1, 2] -> [3, 2, 1]

[1, 2, 3, 4] -> [1, 2, 4, 3]
[2, 1, 3, 5] -> [2, 1, 5, 3]
[2, 5, 3, 1] -> [3, 1, 2, 5]
[5, 3, 1, 2] -> [5, 3, 2, 1]

'''

class Solution:
    """     
    def nextPermutation(self, nums):
        Do not return anything, modify nums in-place instead.
        l = len(nums)
        point = None
        swapped = False
        for i in range(l-1, 0, -1):
            if nums[i] > nums[i-1]:
                if point:
                    # need to find idx well
                    # need to find idx starting from the end of the list
                    # for the cases where the list has duplicated...
                    
                    nums[i-1], nums[idx] = nums[idx], nums[i-1]
                    self.reverse(nums, i+1)
                else:
                    nums[i], nums[i-1] = nums[i-1], nums[i]
                swapped = True
                break
            else: 
                point = True

        if not swapped:
            for i in range(l//2+1):
                nums[i], nums[-i-1] = nums[-i-1], nums[i]
    """

    def nextPermutation(self, nums):
        l = len(nums)
        i = l - 2
        while i >= 0 and nums[i+1] <= nums[i]: # decreasing
            i -= 1
        if i >= 0:      # if it has something to swap
            # search the cloest bigger idx with nums[i]
            # from the end of the list
            # because from (i+1)th element, it should be decreasing order
            # we can take the most backwards but bigger than nums[i]
            j = l - 1
            while (nums[j] <= nums[i]):
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        self.reverse(nums, i+1)
    
    def reverse(self, L, start):
        i, j = start, len(L) - 1
        while (i < j):
            L[i], L[j] = L[j], L[i]
            i += 1
            j -= 1


if __name__ == '__main__':
    L1 = [2, 3, 1, 3, 3]
    # print(Solution().findClosestNum(L1, 2))
    Solution().nextPermutation(L1)
    print(f"next permutation of [2, 3, 1, 3, 3] is {L1}")

    L2 = [2, 5, 3, 1]
    Solution().nextPermutation(L2)
    print(f"next permutation of [2, 5, 3, 1] is {L2}")

    L3 = [2, 1, 2, 2, 2, 2, 2, 1]
    #print(Solution().findClosestNum(L3, 1))
    Solution().nextPermutation(L3)
    print(f"next permutation of [2, 1, 2, 2, 2, 2, 2, 1] is {L3}")

    L4 = [2,3,1]
    Solution().nextPermutation(L4)
    print(f"next permutation of [2, 3, 1] is {L4}")