"""
Problem : Maximum profit by cutting rod.

prices = [
            [1, 2, 5],  --> Rod Length
            [1, 3, 12]  --> Cost
         ]


MP(N) = max(
            P(1) + MP(N-1),
            P(2) + MP(N-2),
            P(5) + MP(N-5)
            )

Branches = Lengths
Levels = N/MinValue  == N if MinValue == 1, logN if MinValue is 2

TC: (Length)^Branches
SC:

"""
import math


class Solution:
    def maxProfit(self, prices, length, N):
        # Base Cases
        if N == 0:
            return 0
        if N < 0:
            return -math.inf

        maxP = 0
        for i in range(length):
            maxP = max(prices[1][i] + self.maxProfit(prices, length, N-prices[0][i]))

        return maxP

    def maxProfitMemo(self, prices, length, N, memo):  # Top-Down Approach
        # Base Cases
        if N < 0:
            return -math.inf
        if N == 0:
            return 0

        if memo[N] < 0:
            maxP = 0
            for i in range(length):
                maxP = max(prices[1][i] + self.maxProfitMemo(prices, length, N - prices[0][i], memo))

            memo[N] = maxP
        return memo[N]

    """
    TC: O(N*length)
    SC: O(N)
    """

    @staticmethod
    def maxProfitDPBottomUp(prices, N):
        memo = [-math.inf for _ in range(N+1)]
        for length in range(1, N+1):
            max_val = 0
            for lengthIdx in range(len(prices)):
                if length > prices[0][lengthIdx]:
                    val = prices[1][lengthIdx] + memo[length-prices[0][lengthIdx]]
                else:
                    val = -math.inf
                max_val = max(max_val, val)
            memo[length] = max_val

        return memo[-1]

    """
    TC: O(length*N)
    SC: O(N)
    """