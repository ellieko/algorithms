'''

Given an array nums of distinct integers,
return all the possible permutations.
You can return the answer in any order.

e.g.
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

'''

class Solution:
    def permute(self, nums):
        def backtrack(l, idxes):
            if len(l) == len(nums):
                results.append(l)
                return
            for i in range(len(nums)):
                if i in idxes:
                    continue
                backtrack(l+[nums[i]], idxes + [i])
        results = []
        backtrack([], [])
        return results
    
    def permute_v2(self, nums):
        def backtrack(first=0):
            if first == len(nums):
                results.append(list(nums))
            for i in range(first, len(nums)):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]
        results = []
        backtrack()
        return results

if __name__ == '__main__':
    print(Solution().permute_v2([1]))
    print(Solution().permute_v2([0, 1]))
    print(Solution().permute_v2([1,2,3]))