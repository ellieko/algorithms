'''
You are given two integer arrays nums1 and nums2,
sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function,
but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n,
where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
'''


class Solution:

    # using pointers (not use sort built-in func)
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        copy = nums1[:m]
        p1, p2 = 0, 0
        for p in range(m+n):
            if p2 >= n or (p1 < m and copy[p1] <= nums2[p2]):
                nums1[p] = copy[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1
        return nums1

    
    # don't overcomplicate the problem
    # they said not to return sorted(arr) but didn't say not to use sort built-in function
    def merge_v2(self, nums1, m: int, nums2, n: int) -> None:
        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1.sort()
        return nums1
        
if __name__ == '__main__':

    print(Solution().merge([-1,-1,0,0,0,0], 4, [-1, 0], 2))       # [-1,-1,-1,0,0,0]
    print(Solution().merge([1,2,3,0,0,0], 3, [2,5,6], 3))         # [1,2,2,3,5,6]
    print(Solution().merge([0,0,0], 0, [2,5,6], 3))               # [2,5,6]
    print(Solution().merge([1], 1, [], 0))                        # [1]
    print(Solution().merge([-2,0,0,0], 2, [-3,1], 2))             # [-3,-2,0,1]
    print(Solution().merge([1,0], 1, [2], 1))                     # [1,2]
    print(Solution().merge([1,2,3,0,0,0], 3, [4,5,6], 3))         # [1,2,3,4,5,6]
    print(Solution().merge([4,0,0,0,0,0], 1, [1,2,3,5,6], 5))     # [1,2,3,4,5,6]  

    print("- - - - - - - - - - - - - - - -")

    print(Solution().merge_v2([-1,-1,0,0,0,0], 4, [-1, 0], 2))     # [-1,-1,-1,0,0,0]
    print(Solution().merge_v2([1,2,3,0,0,0], 3, [2,5,6], 3))       # [1,2,2,3,5,6]
    print(Solution().merge_v2([0,0,0], 0, [2,5,6], 3))             # [2,5,6]
    print(Solution().merge_v2([1], 1, [], 0))                      # [1]
    print(Solution().merge_v2([-2,0,0,0], 2, [-3,1], 2))           # [-3,-2,0,1]
    print(Solution().merge_v2([1,0], 1, [2], 1))                   # [1,2]