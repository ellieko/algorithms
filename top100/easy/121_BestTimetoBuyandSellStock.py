'''
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.

[Constraints]
1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4

'''

class Solution:
    # approach 1) Brute Force --> Time Limit Exceeded
    def maxProfit(self, prices) -> int:
        profit = 0
        for i in range(len(prices)-1):
            temp = max(prices[i+1:]) - prices[i]
            if temp > profit:
                profit = temp
        return profit

    # approach 2)
    def maxProfit_v2(self, prices) -> int:
        min = float('inf')
        profit = 0
        for i in range(len(prices)):
            if prices[i] < min:
                min = prices[i]
            elif prices[i] - min > profit:
                profit = prices[i] - min
        return profit


if __name__ == '__main__':
    print(Solution().maxProfit([7,1,5,3,6,4]))              # 5
    print(Solution().maxProfit_v2([7,1,5,3,6,4]))           # 5
    