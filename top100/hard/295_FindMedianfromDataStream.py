'''
295. Find Median from Data Stream
https://leetcode.com/problems/find-median-from-data-stream/

'''

import heapq

class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []
        
    # time complexity: O(logn)
    def addNum(self, num: int) -> None:
        # add it to maxHeap by default
        heapq.heappush(self.small, -1 * num)                
        
        # move it to minHeap if it violates our rules
        if self.small and self.large and (-1 * self.small[0]) > self.large[0]:
            maxVal = -1 * heapq.heappop(self.small)
            # add the max value of max heap to min heap
            heapq.heappush(self.large, maxVal)
        
        # move it to the place of too smaller length
        if len(self.small) > len(self.large) + 1:
            maxVal = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, maxVal)
            
        # move it to the place of too smaller length
        if len(self.large) > len(self.small) + 1:
            minVal = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * minVal)

            
    # time complexity: O(1)
    def findMedian(self) -> float:
        
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.small) < len(self.large):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0])/2
        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# Time Limit Exeeded
class MedianFinder_v2:

    def __init__(self):
        self.heap = []
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap, num)

    def findMedian(self) -> float:
        copy = self.heap.copy()
        n = len(copy)
        l = []
        for i in range(n):
            l.append(heapq.heappop(copy))
        
        # odd
        if n%2:
            return l[n//2]
        return (l[n//2-1] + l[n//2])/2



# Time Limit Exceeded
class MedianFinder_v1:

    def __init__(self):
        self.data = []
        
    def addNum(self, num: int) -> None:
        
        for i in range(len(self.data)):
            if num < self.data[i]:
                self.data.insert(i, num)
                return
        self.data.append(num)
        
    def findMedian(self) -> float:
        n = len(self.data)
        # odd
        if n%2:
            return self.data[n//2]
        return (self.data[n//2-1] + self.data[n//2])/2
            