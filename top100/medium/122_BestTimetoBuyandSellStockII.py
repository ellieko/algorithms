'''
122. Best Time to Buy and Sell Stock II

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

"!!!On each day!!!", you may decide to buy and/or sell the stock.
You can only hold at most one share of the stock at any time.
However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

'''
# should ask a clarification question "so multiple transactions are possible here"
# the difference than the previous problem (TOP100/easy/121_BestTimeToBuyandSellStock.py)
# is that now you can buy and sell stock multiple times

# [7,1,5,3,6,4]
# 1, 6 (5)             --> 5
# 1, 5 (4) +  3, 6 (3) --> 7

class Solution:
    # approach 1) bruteforce -- time complexity : O(n^n)
    # time limit exceeded
    def maxProfit(self, prices) -> int:
        def calculate_maxprofit(prices, start):
            if start >= len(prices):
                return 0

            max_profit = 0
            for i in range(start, len(prices)):     # loop for possible starting index
                max_profit_with_i = 0               # current profit with decided starting index, i

                for j in range(i+1, len(prices)):   # loop for possible transaction under starting index, i
                    # check every possibility if it makes any profit
                    if prices[i] < prices[j]:       
                        curr_profit = calculate_maxprofit(prices, j+1) + prices[j] - prices[i]

                        # if this profit makes larger profit than the previous saved profit
                        # change the value
                        if curr_profit > max_profit_with_i:
                            max_profit_with_i = curr_profit

                if max_profit_with_i > max_profit:
                    max_profit = max_profit_with_i

            return max_profit
                

        # start calculating with start index 0
        # calculcate with the next element is greater than prices[start]
        # suppose they take this transaction and call the function recursively
        # until start index hits len(prices), which means where it can't add anything anymore
        return calculate_maxprofit(prices, 0)

    # approach 2) one pass -- time complexity : O(n)
    def maxProfit_v2(self, prices) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            # if it's ascending
            if prices[i-1] < prices[i]:
                max_profit += prices[i] - prices[i-1]
        return max_profit


if __name__ == '__main__':
    print(Solution().maxProfit([7,1,5,3,6,4]))          # 7
    print(Solution().maxProfit_v2([7,1,5,3,6,4]))       # 7
    # [7, 1, 5, 5, 6, 1]

    # [1, 7, 2, 3] --> 7
    # [1, 7, 2, 3, 6, 7, 6, 7]