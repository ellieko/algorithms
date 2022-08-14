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
    # time complexity: O(N) in average case and O(N^2) in the worst case