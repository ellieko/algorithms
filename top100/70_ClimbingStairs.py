'''

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

'''

class Solution:
    # brute force - O(2^n)
    def climbStairs(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n-1)+self.climbStairs(n-2)

    # Dynamic Programming - O(n)
    def climbStairs_v2(self, n):
        L = [1,2]
        for i in range(2, n):
            L.append(L[i-1]+L[i-2])
        return L[n-1]

if __name__ == '__main__':
    print(Solution().climbStairs_v2(1))
    print(Solution().climbStairs_v2(2))
    print(Solution().climbStairs_v2(3))
    print(Solution().climbStairs_v2(4))
