#Answer to this - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/ 
#You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
#On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
#Find and return the maximum profit you can achieve.


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0 
        j = 1
        profit = [0]
        while j <= len(prices)-1 :
            if prices[i] > prices[j] :
                i = i + 1
            else :
                if j == len(prices)-1 :
                    profit[0] = profit[0] + (prices[j] - prices[i])
                    j = j + 1
                elif prices[j] > prices[j + 1]:
                    profit[0] = profit[0] + (prices[j] - prices[i])
                    i = j
                    j = j + 1
                else :
                    j = j + 1

        return max(profit)
