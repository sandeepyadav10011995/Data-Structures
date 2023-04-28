"""
Grids unique Paths
Approach 1: DFS

Approach 2: DFS using Memo

Approach 3: Mathematical Solution -> Combination
            Observation 1 : Total = N+M-2
            Observation 2: R = Right Pass or Bottom Pass

            Total
                (C)     = total!
                   R      total-r! * r !
"""


class Solution:
    def countPaths(self, i, j, n, m) -> int:
        # Base Case
        if i == n-1 and j == m-1: return 1
        if i >= n or j >= m: return 0

        return self.countPaths(i+1, j, n, m) + self.countPaths(i, j+1, n, m)

    def countPathsWithMemo(self, i, j, n, m, dp) -> int:
        if i == n - 1 and j == m - 1: return 1
        if i >= n or j >= m: return 0

        if dp[i][j] < 0:
            dp[i][j] = self.countPathsWithMemo(i+1, j, n, m , dp) + self.countPathsWithMemo(i, j+1, n, m, dp)
        return dp[i][j]

    @staticmethod
    def countPathsMathematicalSol(m, n):
        N = n+m-2
        R = m-1
        res = 1

        for i in range(R+1):
            res *= (N-R+i)/i
        return int(res)

