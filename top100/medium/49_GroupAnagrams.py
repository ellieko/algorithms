'''
49. Group Anagrams
https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

'''

from typing import List


class Solution:

    # 1) Hashmap with sort
    # time complexity: O(m*nlogn)
    # where n is the average length of each of the input strings (or maximum length of the input string)
    # and m is the length of the input list

    # space complexity: O(m*n)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        d = defaultdict(list)
        for s in strs:
            d[tuple(sorted(s))].append(s)
        return d.values()
    

    # 2) Better solution where we don't need to sort
    # instead of dictionary to keep track of each frequencies
    # we use list of ord values

    # time complexity: O(m*n*26) -> O(m*n)
    # where n is the maximum length of the input string
    # and m is the length of the input list

    # space complexity: O(m*n)
    def groupAnagrams_v2(self, strs):
        from collections import defaultdict
        ans = defaultdict(list)
        for s in strs:
            count = [0]*26      # use the constraint that there will be at most 26 characters only
            for c in s:
                count[ord(c)-ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()
