'''
217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

'''

class Solution:
    def containsDuplicate(self, nums) -> bool:
        from collections import Counter
        return Counter(nums).most_common()[0][1] > 1

    # time complexity: O(n)
    # space complexity: O(n)
    def containsDuplicate_v2(self, nums) -> bool:
        storage = set()
        for n in nums:
            if n in storage:
                return True
            storage.add(n)
        return False