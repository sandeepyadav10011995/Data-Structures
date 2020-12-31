class Solution:
    def minCoinsBottomUp(self, coins, amount):
        dp = [amount+1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount+1):
            for j in range(len(coins)):
                if coins[j] <= i:
                    dp[i] = min(dp[i], 1+dp[i-coins[j]])
        if dp[-1] > amount:
            return -1
        return dp[-1]

    def _minCoinsTopDown(self, coins, remainder, dp):
        if remainder < -1:
            return -1
        if remainder == 0:
            return 0
        if dp[remainder] != 0:
            return dp[remainder]
        minimum = float('inf')
        for coin in coins:
            change = self._minCoinsTopDown(coins, remainder-coin, dp)
            if 0 <= change < minimum:
                minimum = 1 + change
        if minimum == float('inf'):
            dp[remainder] = -1
        dp[remainder] = minimum
        return dp[remainder]

    def minCoinsTopDown(self, coins, amount):
        if amount < 1:
            return 0
        dp = [0] * (amount+1)
        return self._minCoinsTopDown(coins, amount, dp)

sol = Solution()
amount = 11
coins = [1,2,5]
# DP --> Bottom UP
# print(sol.minCoinsBottomUp(coins, amount))
# DP --> Top Down
print(sol.minCoinsTopDown(coins, amount))
