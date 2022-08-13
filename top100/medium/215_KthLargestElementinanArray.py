'''
215. Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array/

Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
You must solve it in O(n) time complexity.

e.g. nums = [3,2,1,5,6,4], k = 2            --> 5
e.g. nums = [3,2,3,1,2,4,5,5,6], k = 4      --> 4

'''

import heapq


class Solution:
    # quickselect
    # average time complexity: O(n)
    # worst time complexity: O(n^2)
    def findKthLargest(self, nums, k: int) -> int:
        k = len(nums) - k       # index for return value from sorted list

        def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            if p < k:   return quickSelect(p + 1, r)
            elif p > k: return quickSelect(l, p - 1)
            else:       return nums[p] 

        return quickSelect(0, len(nums)-1)

    # heap
    # time complexity: O(nlogn)
    # space complexity: O(n)
    def findKthLargest_v1(self, nums, k: int) -> int:
        h, res = [], []
        for n in nums:
            heapq.heappush(h, -n)
            
        for i in range(len(h)):
            res.append(-heapq.heappop(h))
        return res[k-1]

    # heap
    # time complexity: O(nlogn)
    # space complexity: O(n)
    def findKthLargest_v2(self, nums, k: int) -> int:
        heapq.heapify(nums)
        for i in range(len(nums)-k):
            heapq.heappop(nums)
        return heapq.heappop(nums)

