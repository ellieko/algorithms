'''
253. Meeting Rooms II
https://leetcode.com/problems/meeting-rooms-ii/

Given an array of meeting time intervals intervals where intervals[i] = [starti, endi],

return the minimum number of conference rooms required.

e.g. intervals = [[0, 30], [5, 10], [15, 20]]       --> 2
e.g. intervals = [[7, 10], [2, 4]]                  --> 1

'''


from typing import List


class Solution:
    # the maximum number of overlapping meetings at any given point in time
        
    # time complexity: O(nlogn)
    # space complexity: O(n)
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        start = sorted([i for i, j in intervals])
        end = sorted([j for i, j in intervals])
        i = j = count = maxCount = 0
        while i < len(start):
            if start[i] < end[j]:
                count += 1
                i += 1
                maxCount = max(count, maxCount)
            else:
                count -= 1
                j += 1
        return maxCount
