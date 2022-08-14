'''
347. Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/

Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

문제 이해 - k번 등장하는 원소들이 아니고, 자주 등장하는 순서대로 k개 까지만...

'''

class Solution:
    # my approach - using Counter
    # time complexity: O(nlogn)
    # space complexity: O(n)
    def topKFrequent_v1(self, nums, k: int):
        from collections import Counter
        c = Counter(nums).most_common()
        ans = []
        for i in range(k):
            ans.append(c[i][0])
        return ans

    # another approcah - w/o using Counter
    # time complexity: O(nlogn)
    # space complexity: O(n)
    def topKFrequent_v2(self, nums, k: int):
        c = {}
        for n in nums:
            c[n] = c.get(n,0) + 1
        l = list(c.items())
        l.sort(key = lambda x: x[1], reverse=True)
        return [l[i][0] for i in range(k)]

    # max heap
    # time complexity: O(klogn)
    # space complexity: O(n+k) to store the hash map with n elements and a heap with k elements
    def topKFrequent_v3(self, nums, k: int):
        import heapq
        # pop k elements from heap
        # where higher frequency is prioritized
        c = {}
        for n in nums: 
            c[n] = c.get(n, 0) + 1
        
        h = ans = []
        for elem, count in c.items():
            heapq.heappush(h, (-count, elem))
            
        for i in range(k):
            ans.append(heapq.heappop(h)[1])
        return ans

    
    # better approach - bucket sort -> good!!!!!
    # with using index for occurrences (counts) and value for a list of elements occurred for the occurrence
    # time complexity: O(n)
    # space complexity: O(n)
    def topKFrequent_v4(self, nums, k: int):
        # counter dict
        c = {}
        for n in nums:
            c[n] = 1 + c.get(n,0)
            
        # frequencies to elements
        # make sure not to use same variable names (i.e., k)
        freq_to_elems = [[] for _ in range(len(nums)+1)]
        for elem, count in c.items():
            freq_to_elems[count].append(elem)

        # make res to return
        res = []
        for i in range(len(freq_to_elems)-1, 0, -1):
            for elem in freq_to_elems[i]:
                res.append(elem)
                if len(res) == k:
                    return res


if __name__ == '__main__':
    print(Solution().topKFrequent_v3([1,1,1,2,2,3], 2))