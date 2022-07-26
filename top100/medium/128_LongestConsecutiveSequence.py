'''
128. Longest Consecutive Sequence

Given an unsorted array of integers nums,
return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.


'''

class Solution:
    # my approach
    # time complexity: O(n)
    # space complexity: O(n)
    def longestConsecutive_v1(self, nums) -> int:
        import heapq
        # always consist of distinct values?
        # --> no, it didn't say so
        # [0, 1, 1, 2] -> expected result is 3
        
        if len(nums) < 2:
            return len(nums)
        
        max_len = tmp_len = 1
        heapq.heapify(nums)
        prev = heapq.heappop(nums)
        
        while nums:
            curr = heapq.heappop(nums)
            
            if prev + 1 == curr:    # if prev and curr are consecutive
                tmp_len += 1        #    increase tmp_len
            elif prev == curr:      # elif they are the same val
                continue            #    go on to next elem
            else:
                # update max_len and reset the tmp_len
                max_len = max(max_len, tmp_len)
                tmp_len = 1
                
            prev = curr
                
        max_len = max(max_len, tmp_len)
        return max_len


    # another approach using set only
    # time complexity: O(n)
    # space complexity: O(n)
    def longestConsecutive_v2(self, nums) -> int:
        s = set(nums)
        max_len = 0
        for n in nums:
            # if its the start of a sequence
            if n-1 not in s:
                length = 1
                while (n + length) in s:
                    length += 1
                max_len = max(max_len, length)
                
        return max_len
        
        