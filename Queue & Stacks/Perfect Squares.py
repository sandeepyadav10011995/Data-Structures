"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:
Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

"""
class Solution:
    def numSquares(self, n: int) -> int:
        if n==1:
            return 1
        squares = [i*i for i in range(1, (n//2)+1) if i*i <= n]
        dp = [float(inf) for _ in range(n+1)]
        dp[0] = 0
        for square in squares:
            for num in range(square, n+1):
                dp[num] = min(dp[num], dp[num-square]+1)
                
        return dp[-1]
