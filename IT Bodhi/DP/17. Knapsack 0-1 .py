"""
Problem : Knapsack 0/1

Capacity = 10
W   4   3   6   8   5   10  5   1
V   1   2   4   2   2   6   12  3
idx 0   1   2   3   4   5   6   7



Approach 1: Recursive
        TC: O(2^N)
        SC: O(N)

Approach 2: Top-Down
        TC: O(2*N*Capacity)
        SC: O(N*Capacity)

Approach 3: Bottom Up
        TC: O(N*Capacity)
        SC: O(N*Capacity)
"""


class Solution:
    def _knapSack01Recursive(self, profits, weights, capacity, curIdx):
        # Base Case
        if capacity <= 0 or curIdx >= len(profits):
            return 0

        # recursive call after choosing the element at the currentIndex
        # if the weight of the element at currentIndex exceeds the capacity, we  shouldn't process this
        profit1 = 0
        if weights[curIdx] <= capacity:
            profit1 = profits[curIdx] + \
                      self._knapSack01Recursive(profits, weights, capacity - weights[curIdx], curIdx + 1)

        # recursive call after excluding the element at the currentIndex
        profit2 = self._knapSack01Recursive(profits, weights, capacity, curIdx + 1)

        return max(profit1, profit2)

    def solveKnapSack01(self, profits, weights, capacity):
        return self._knapSack01Recursive(profits, weights, capacity, curIdx=0)

    def _knapSack01RecursiveMemo(self, memo, profits, weights, capacity, curIdx):
        # Base Case
        if capacity <= 0 or curIdx >= len(profits):
            return 0

        if memo[curIdx][capacity] < 0:
            # recursive call after choosing the element at the currentIndex
            # if the weight of the element at currentIndex exceeds the capacity, we  shouldn't process this
            profit1 = 0
            if weights[curIdx] <= capacity:
                profit1 = profits[curIdx] + \
                          self._knapSack01Recursive(memo, profits, weights, capacity - weights[curIdx], curIdx + 1)

            # recursive call after excluding the element at the currentIndex
            profit2 = self._knapSack01Recursive(memo, profits, weights, capacity, curIdx + 1)
            memo[curIdx][capacity] = max(profit1, profit2)

        return memo[curIdx][capacity]

    def solveKnapSack01Memo(self, profits, weights, capacity):
        memo = [[-1 for _ in range(capacity+1)] for _ in range(len(profits))]
        return self._knapSack01RecursiveMemo(memo, profits, weights, capacity, curIdx=0)

    @staticmethod
    def solveKnapSack01BottomUp(profits, weights, capacity):
        N = len(profits)
        # Base Case
        if capacity <= 0 or N == 0 or N != len(weights):
            return 0

        memo = [[0 for _ in range(capacity+1)] for _ in range(N)]
        # Populate the capacity = 0 columns with 0 profits
        for i in range(N):
            memo[i][0] = 0

        # If we have only one weight then we will take it's profit if it is not more than the capacity
        for c in range(capacity+1):
            if weights[0] <= c:
                memo[0][c] = profits[0]

        # Process all the sub-arrays for all the capacities
        for i in range(1, N):
            for c in range(1, capacity+1):
                profit1, profit2 = 0, 0
                # Include The Item
                if weights[i] < c:
                    profit1 = profits[i] + memo[i-1][c-weights[i]]
                # Exclude the item
                profit2 = memo[i-1][c]

                memo[i][c] = max(profit1, profit2)

        # maximum profit will be in the bottom-right corner.
        return memo[-1][-1]

