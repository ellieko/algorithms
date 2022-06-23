'''
169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

* constraints
n == nums.length
1 <= n <= 5 * 104
-10^9 <= nums[i] <= 10^9

'''


class Solution:
    # approach 1) what i did
    # time complexity of O(N) space with space complexity of O(N)
    def majorityElement(self, nums) -> int:
        from collections import Counter
        c = Counter(nums)
        # return c.most_common()[0][0]
        return max(c.keys(), key=c.get) # return key having the maximum value

        # takeaway - usage of key parameter in max
        # d = {'aim':99,'artwork':23}
        # max(d.keys(), key=lambda x: len(x)) -- return 'artwork' (key having the longest length)

    # approach 2) sorting
    # [2,2,1,1,1,2,2] --> sort --> [1,1,1,2,2,2,2]      len//2 = 7//2 = 3
    # [2,3,3,0]       --> sort --> [0,2,3,3]            len//2 = 4//2 = 2
    def majorityElement_v2(self, nums) -> int:
        nums.sort()
        return nums[len(nums)//2]

    # approach 3) Boyer-Moore Voting Algorithm
    # time complexity of O(N) with space compexity of O(1)
    # if len == even: elem has to appear more than half (len == 4 --> elem has to appear 3 or 4 times not 2)
    def majorityElement_v3(self, nums) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if candidate == num else -1
        return candidate

            
if __name__ == '__main__': 
    print(Solution().majorityElement([2,2,1,1,1,2,2]))          # 2
    print(Solution().majorityElement_v2([2,2,1,1,1,2,2]))
    print(Solution().majorityElement_v3([2,2,1,1,1,2,2]))

    print(Solution().majorityElement([3,2,3]))                  # 3
    print(Solution().majorityElement_v2([3,2,3]))
    print(Solution().majorityElement_v3([3,2,3]))