"""
Problem: Max profit by buying & selling stock once
Ex: Stock Prices = [5   3   4   6   8   5   7   2   3   6]
        Profit =   [MIN -2  1   3   5   2   4  -1   1   4]
        minSoFar=   MIN  5  3   3   3   3   3   3   2   2
Approach -: Brute Force
            Keep checking minSoFar for (1, N)
            Then find the max from the profits
            TC: O(N)
            SC: O(N) --> Remove it by using a variable maxProfitSoFar
"""
import math


class Solution:
    @staticmethod
    def maxProfitBuyAndSellStocksOnce(stockPrices):
        N = len(stockPrices)
        minStockPriceSoFar = math.inf
        maxProfitSoFar = -math.inf

        for i in range(N):
            curProfit = stockPrices[i] - minStockPriceSoFar
            maxProfitSoFar = max(maxProfitSoFar, curProfit)
            minStockPriceSoFar = min(minStockPriceSoFar, stockPrices[i])

        return maxProfitSoFar
    """
    TC: O(N)
    SC: O(1)
    """


sol = Solution()
print(sol.maxProfitBuyAndSellStocksOnce(stockPrices=[5, 3, 4, 6, 8, 5, 7, 2, 3, 6]))
