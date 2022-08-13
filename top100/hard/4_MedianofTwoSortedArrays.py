'''
4. Median of Two Sorted Arrays
https://leetcode.com/problems/median-of-two-sorted-arrays/


Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
  
The overall run time complexity should be O(log (m+n)).
'''

class Solution:
    # time complexity: O(log(min(n, m)))
    # space complexity: O(n + m) for A and B
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A
        
        total = len(A)+len(B)
        half = total//2
        
        l, r = 0, len(A) - 1
        while True:
            i = (l + r)//2      # A
            j = half - i - 2    # B
            
            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i+1] if (i + 1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j+1] if (j + 1) < len(B) else float("inf")
            
            if Aleft <= Bright and Bleft <= Aright:
            
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright))/2
                
            elif Aleft > Bright:
                r = i - 1
            
            else:
                l = i + 1