'''
496. Next Greater Element I
https://leetcode.com/problems/next-greater-element-i/

'''

from typing import List

 
class Solution:
    # bruteforce

    # time complexity: O(n*m)
    # space complexity: O(m)
    # where m and n is respectively the length of nums1 and nums2
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        res = [-1] * len(nums1)
        mapToIndex = {n:i for i, n in enumerate(nums1)}
        for i in range(len(nums2)):
            if nums2[i] not in mapToIndex: continue
            for j in range(i+1, len(nums2)):
                if nums2[j] > nums2[i]:
                    res[mapToIndex[nums2[i]]] = nums2[j]
                    break
        return res

    # monotonic stack techinque
    # time complexity: O(m+n)
    # space complexity: O(m)
    def nextGreaterElement_optimized(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        mapToIndex = {n:i for i,n in enumerate(nums1)}
        stack = []
        
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                res[mapToIndex[val]] = cur
            if cur in mapToIndex:
                stack.append(cur)
        return res

