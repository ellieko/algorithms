'''
973. K Closest Points to Origin
https://leetcode.com/problems/k-closest-points-to-origin/

'''

from typing import List


class Solution:
    # sort
    # time complexity: O(nlogn)
    # space complexity: O(n)
    def kClosest_v1(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        for idx, point in enumerate(points):
            distance.append((point[0]**2+point[1]**2, idx))
        distance.sort()
        
        return [points[d[1]] for d in distance[:k]]

    # min heap
    # time complexity: O(klogn)
    # space complexity: O(n)
    def kClosest_v2(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        h, res = [], []
        for x,y in points:
            dist = abs(x)**2 + abs(y)**2
            h.append((dist, x, y))
        heapq.heapify(h)
        for _ in range(k):
            dist, x, y = heapq.heappop(h)
            res.append([x, y])
        return res

    # divide and conqueer
    # quickselect (using the fact that the k elements returned can be in any order)
    # time complexity: O(N) in average case and O(N^2) in the worst case -- TLE
    def kClosest_v3(self, points: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(points)):
            dist = points[i][0]**2 + points[i][1]**2
            points[i] = (dist, points[i][0], points[i][1])

        res = []
        
        def quickSelect(l, r):
            if l > r: return
            p = l
            for i in range(l, r):
                if points[i][0] <= points[r][0]:
                    points[i], points[p] = points[p], points[i]
                    p += 1
            points[r], points[p] = points[p], points[r]
            if p < k:
                quickSelect(p + 1, r)
            else:
                quickSelect(l, p - 1)
        
        quickSelect(0, len(points)-1)
        
        return [(x,y) for _, x, y in points[:k]]
        