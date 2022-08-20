'''
3. 3 Sum
https://leetcode.com/problems/3sum/solution/

Given an integer array nums,
return all the triplets [nums[i], nums[j], nums[k]] such that
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

e.g.
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

'''

from typing import List


class Solution:

    # sort first and use two pointers w/o set
    # time complexity: O(n^2)
    # space complexity: O(n) due to sorting
    def threeSum_v1(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        # fix the first index i
        for i in range(len(nums)-2):
            
            # if we already consider this first value, pass
            if i > 0 and nums[i-1] == nums[i]: continue
                
            # start with the fixed first element
            j, k = i+1, len(nums)-1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    res.append((nums[i], nums[j], nums[k]))
                    # still need to check other values 
                    j += 1
                    # but if new jth value is the same as the previous jth value,
                    # we don't need to check because we have already checked
                    while nums[j] == nums[j-1] and j < k:
                        j +=1

        return res

    # sort first and use two pointers w/ set
    # time complexity: O(n^2)
    # space complexity: O(n) due to sorting
    def threeSum_v2(self, nums):
        res = set()
        nums.sort()

        # fix the first index i
        for i in range(len(nums)-2):
            
            # if we already consider this first value, pass
            if i > 0 and nums[i-1] == nums[i]: continue
                
            # start with the fixed first element
            j, k = i+1, len(nums)-1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    res.add((nums[i], nums[j], nums[k]))
                    # still need to check other values 
                    j += 1
                    k -= 1
                    # but there may still have duplicates when these new jth and kth values are the same as the previous values of them
                    # that's why we are using set for our res

        return res


    # same approach but using helper function
    # time complexity: O(n^2)
    # space complexity: O(n)
    def threeSum_v3(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:                     # because can't make its sum = 0 with positive number being the smallest
                break
            if i == 0 or nums[i-1] != nums[i]:  # make sure no duplicate, no first element that we already checked
                self.twoSum_v2(nums, i, res)
        return res

    # helper function version 1 (two pointers)
    def twoSum_v1(self, nums, i, res) -> None:
        lo, hi = i+1, len(nums) - 1
        while lo < hi:
            total = nums[i] + nums[lo] + nums[hi]
            if total < 0:
                lo += 1
            elif total > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1        
                hi -= 1                       # change both pointers because we can't have duplicate
                while lo < hi and nums[lo] == nums[lo-1]:   # if there's more duplicates of nums[lo]
                    lo += 1

    # helper function version 2 (hashmap)
    def twoSum_v2(self, nums, i, res) -> None:
        seen = set()
        j = i+1
        while j < len(nums):
            complement = - nums[i] - nums[j]
            if complement in seen:
                res.append([nums[i], nums[j], complement])
                while j < len(nums) and nums[j] == nums[j+1]:   # increment j until nums[j] to be a new element
                    j +=1
            seen.add(nums[j])
            j +=1 

    
    # w/o sort
    # if you are not allowed to modify the input array, and you want to avoid copying it due to memory constraints?
    # it's possible, though the efficiency would heavily depend on the input
    # If we have a very large array with many duplicates and a few matching triplets,
    # the "no-sort" approach would be more memory efficient

    # e.g. [1,0,-2,1,2] --> [-2,0,1,1,2] ---> should return [[-2,0,2],[-2,1,1]]

    # time complexity: O(n^2)
    # space complexity: O(n)
    def threeSum_v4(self, nums):
        res = set()
        # having a target as -nums[i],
        # now we can find two elements whose sum is -nums[i], but three numbers should be something I haven't seen yet
        for i in range(len(nums)-2):
            seen = set()    # for making sum of -nums[i]
            for j in range(i+1, len(nums)):
                complement = -nums[i]-nums[j]
                if complement in seen:
                    temp = [nums[i], nums[j], complement]
                    temp.sort()
                    res.add(tuple(temp))    
                else:
                    seen.add(nums[j])
        return res

    # an optimized version of threeSum_v4 (w/o sort)
    # Instead of re-populating a hashset every time in the inner loop,
    # we can use a hashmap and populate it once.
    # Values in the hashmap will indicate whether we have encountered that element in the current iteration.
    # When we process nums[j] in the inner loop, we set its hashmap value to i.
    # This indicates that we can now use nums[j] as a complement for nums[i].
    # This is more like a trick to compensate for container overheads.
    def threeSum_v4_optimized(self, nums):
        res, dups = set(), set()
        seen = {}
        for i,val1 in enumerate(nums):
            if val1 not in dups:        # if it's in dups, it means we already checked the sum, continue
                dups.add(val1)
                for j,val2 in enumerate(nums[i+1:]):
                    complement = -val1-val2
                    if complement in seen and seen[complement] == i:    # if we've seen complement during ith iteration
                        res.add(tuple(sorted((val1,val2, complement))))
                    seen[val2] = i
        return res



if __name__ == '__main__':
    print(Solution().threeSum_v1([-1,0,1,2,-1,-4]))    # should return [[-1,0,1], [-1,-1,2]]
    print(Solution().threeSum_v1([0,0,0,0]))           # should return [[0,0,0]]
    print(Solution().threeSum_v1([-2,0,1,1,2]))        # should return [[-2,0,2],[-2,1,1]]

    print(Solution().threeSum_v3([-1,0,1,2,-1,-4]))    # should return [[-1,0,1], [-1,-1,2]]
    print(Solution().threeSum_v3([0,0,0,0]))           # should return [[0,0,0]]
    print(Solution().threeSum_v3([-2,0,1,1,2]))        # should return [[-2,0,2],[-2,1,1]]