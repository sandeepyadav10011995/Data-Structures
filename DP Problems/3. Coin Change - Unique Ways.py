class Solution:
    def coinChange(self, coins, amount):
        dp = [[0] * (amount+1) for _ in range(len(coins)+1)]
        # Max ways to make change for 0 will be 1, doing nothing.
        dp[0][0] = 1
        for i in range(1, len(coins)+1):
            dp[i][0] = 1
            for j in range(1, amount+1):
                with_coin = dp[i][j-coins[i-1]]
                without_coin = dp[i-1][j]
                dp[i][j] = with_coin + without_coin
        return dp[-1][-1]

sol = Solution()
amount = 5
coins = [1, 2, 5]
print(sol.coinChange(coins, amount))
