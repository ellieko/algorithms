'''
56. Merge Intervals

'''

class Solution:
    # time complexity: O(NlogN)
    # space complexity: O(N)
    def merge(self, intervals):
        res = []
        prev = None
        intervals.sort()
        for step in intervals:
            start, end = step[0], step[1]
            if prev == None or prev < start:        # prev == None instead of not None (because prev can be 0)
                res.append([start, end])
                prev = end
            else:   # prev >= start
                res[-1][1] = max(res[-1][1], end)
                prev = res[-1][1]
        return res

if __name__ == '__main__':
    print(Solution().merge([[0,2],[2,3],[4,4],[0,1],[5,7],[4,5],[0,0]]))
        