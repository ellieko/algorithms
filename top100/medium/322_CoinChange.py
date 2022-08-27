'''
322. Coin Change
https://leetcode.com/problems/coin-change/

'''

from typing import List


class Solution:

    # if we think about brutefore solution
    # we will repeat the same calculation
    # so we use DP bottom top solution

    # initially, I approached the problem with greedy
    # but it doesn't work because there's no promise that we will take largest possible times of larger coins
    # e.g. [419, 408, 186, 83], 6249
    # they don't use its quotient, use some of them, and other coins


    # time complexity: O(amount * size of coins)
    # space complexity: O(amount)
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [amount + 1] * (amount + 1)
        
        # we can make amount 0 with 0 number of coins
        dp[0] = 0
        
        for amt in range(1, amount + 1):
            for c in coins:
                if amt - c >= 0:    # for now, to make this amt, can we use this coin c?
                    dp[amt] = min(dp[amt], 1 + dp[amt-c])
        
        return dp[amount] if dp[amount] != amount + 1 else -1