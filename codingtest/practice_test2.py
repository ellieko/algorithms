'''

Given an array of integers nums and a target value k
determine if the array contains a contiguous subarray
such that the sum of the elements of this subarray is k

Eg,
Input: nums=[6,1,3,-2,-1,3,5], k=2
Output: True
Explanation:
1+3-2=2=k

Input: nums=[-1,2,6,-5], k=5
Output: False
Explanation:
No such contiguous subarray exists

'''

def hasSum(nums, k):
    for i in range(len(nums)):
        if nums[i] == k:
            return True
        for j in range(i+1, len(nums)):
            if sum(nums[i:j+1]) == k:
                return True
    return False


# LeetCode Medium: 560. Subarray Sum Equals K
# Given an array of integers nums and an integer k,
# return the total number of continuous subarrays whose sum equals to k.
# Time complexity: O(n^2) -- need faster one (Java passes time limit...)
def subarraySum(nums, k):
    l = len(nums)
    count = 0
    for i in range(l):
        total  = nums[i]
        if total == k:
            count +=1
        for j in range(i+1, l):
            total += nums[j]
            if total == k:
                count += 1
    return count

# use hashmap! (had a hard time understanding...)
def subarraySum_v2(nums, k):
    cumul = {0:1}
    count, total = 0, 0
    for num in nums:
        total += num
        if total - k in cumul:
            count += cumul[total-k]
        cumul[total] = cumul[total] + 1 if total in cumul else 1
    return count

if __name__ == '__main__':
    print(hasSum([6,1,3,-2,-1,3,5], 2))
    print(hasSum([-1,2,6,-5], 5))

    print(subarraySum_v2([1,2,1,2,1],3))
    print(subarraySum_v2([1],0))
    print(subarraySum_v2([1,-1,0], 0))