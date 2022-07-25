'''
49. Group Anagrams
https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

'''

class Solution:
    # my approach
    def groupAnagrams(self, strs):
        from collections import defaultdict
        res = defaultdict(list)
        for word in strs:
            counter = defaultdict(int)
            for c in word:
                counter[c] += 1
            res[tuple(sorted(counter.items()))].append(word)
        return res.values()
    
    # better approach where we don't need to sort
    # instead of dictionary to keep track of each frequencies
    # we use list of ord values
    # time complexity:
    # space complexity:
    def groupAnagrams_v2(self, strs):

        # time complexity: O(nk)
        # space complexity: O(nk)
        # where n is length of strs and k is the maximum length of a string in strs
        from collections import defaultdict
        ans = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()
