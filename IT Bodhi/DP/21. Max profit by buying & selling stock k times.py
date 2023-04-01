"""
Problem : Max profit by buying & selling stock k times/k transactions
Ex-: Ex: Stock Prices = [5, 11, 3, 50, 60, 90], K=2
Indexes represent the --> days.

    5,  11, 3,  50, 60, 90
0   0   0   0   0   0   0
1   0   6   6   47  57  87
2   0   6   6   53  63  93

d=4
60 + max(x=0--> -5+0 = -5
         x=1--> -11+6 = -5
         x=2--> -3+6 = 3
         x=3--> -50+47 = -3
         )
60 + 3 = 63

d=5
90 + max(x=0--> -5+0 = -5
         x=1--> -11+6 = -5
         x=2--> -3+6 = 3
         x=3--> -50+47 = -3
         x=4--> -60+57 = -3
         )
90 + 3 = 93

Formula -: Profit[t][d] = max( 1. Profit[t][d-1]  # Profit from previous days
                               2. Prices[d] + max(-Prices[x] + Profit[t-1][x]) :: 0 <= x < d
TC: O(N*K) --> Wrong
    O(N*K) * O(N) ~ O(N^2*K)
SC: O(N*K)

Can we do better ?
Solution: We can keep a track of maxProfitSoFar


Can you better in Space?
Using two array
TC: O(2N)

"""
import math


class Solution:
    @staticmethod
    def maxProfitWithKTransactionsBF(prices, k):
        # Base Case
        N = len(prices)
        if N == 0:
            return 0

        profits = [[0 for _ in range(N)] for _ in range(k + 1)]

        for t in range(1, k + 1):
            for d in range(1, N):
                maxThusFar = -math.inf
                for x in range(d):
                    maxThusFar = max(maxThusFar, -prices[x] + profits[t-1][x])
                profits[t][d] = max(profits[t][d - 1],
                                    prices[d] + maxThusFar)  # max(previous day, prices[d] + maxThusFar)

        return profits[-1][-1]
    """
    TC: O(N^2*K)
    SC: O(N*K)
    """

    @staticmethod
    def maxProfitWithKTransactions(prices, k):
        # Base Case
        N = len(prices)
        if N == 0:
            return 0

        profits = [[0 for _ in range(N)] for _ in range(k + 1)]

        for t in range(1, k + 1):
            maxThusFar = -math.inf
            for d in range(1, N):
                maxThusFar = max(maxThusFar, profits[t - 1][d - 1] - prices[d - 1])
                profits[t][d] = max(profits[t][d - 1],
                                    prices[d] + maxThusFar)  # max(previous day, prices[d] + maxThusFar)

        return profits[-1][-1]

    @staticmethod
    def maxProfitWithKTransactionsOptimized(prices, k):
        # Base Case
        N = len(prices)
        if N == 0:
            return 0

        evenProfits = [0 for _ in range(N)]
        oddProfits = [0 for _ in range(N)]

        for t in range(1, k + 1):
            maxThusFar = -math.inf
            if t % 2 == 1:
                curProfits = oddProfits
                prevProfits = evenProfits
            else:
                curProfits = evenProfits
                prevProfits = oddProfits

            for d in range(1, N):
                maxThusFar = max(maxThusFar, prevProfits[d - 1] - prices[d - 1])
                curProfits[d] = max(curProfits[d - 1], maxThusFar + prices[d])

        return evenProfits[-1] if k % 2 == 0 else oddProfits[-1]


sol = Solution()
print(sol.maxProfitWithKTransactionsBF(prices=[5, 11, 3, 50, 60, 90], k=2))
print(sol.maxProfitWithKTransactions(prices=[5, 11, 3, 50, 60, 90], k=2))
print(sol.maxProfitWithKTransactionsOptimized(prices=[5, 11, 3, 50, 60, 90], k=2))
