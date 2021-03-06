'''
11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/

You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line
are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container,
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

'''


class Solution:

    # Brute Force: Time limit excedded - O(n^2)
    def maxArea_v1(self, height):
        l = len(height)
        ans = 0
        for i in range(l-1):
            for j in range(i+1, l):
                temp = (j-i)*min(height[j], height[i])
                if ans < temp:
                    ans = temp
        return ans

    # max area will be made with biggest width or biggest height 
    # time complexity: O(n)
    # space complexity: O(1)
    def maxArea_v2(self, height):
        maxarea, l, r = 0, 0, len(height) - 1
        while (l < r):
            maxarea = max(maxarea, (r-l)* min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxarea

if __name__ == '__main__':
    print(Solution().maxArea_v1([2,3,4,5,18,17,6]))