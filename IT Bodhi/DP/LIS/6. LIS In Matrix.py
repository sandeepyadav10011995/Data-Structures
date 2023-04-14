import math


class Solution:
    def __init__(self, _matrix):
        self.dp = None
        self.matrix = _matrix
        self.rows = len(_matrix)
        self.cols = len(_matrix[0])

    def _dfs(self, i: int, j: int, prev: int) -> int:
        # Base Case
        if i < 0 or i >= self.rows or j < 0 or j >= self.cols:
            return 0
        # Edge Case
        if self.matrix[i][j] <= prev:
            return 0

        if self.dp[i][j] < 0:
            curr = self.matrix[i][j]
            self.dp[i][j] = 1 + max(self._dfs(i + 1, j, curr),
                                    self._dfs(i - 1, j, curr),
                                    self._dfs(i, j + 1, curr),
                                    self._dfs(i, j - 1, curr))
        return self.dp[i][j]

    def longestIncreasingPath(self) -> int:
        self.dp = [[-1 for _ in range(self.rows)] for _ in range(self.cols)]

        return max(self._dfs(row, col, -math.inf) for row in range(self.rows) for col in range(self.cols))


matrix = [
    [9, 9, 4],
    [6, 6, 8],
    [2, 1, 1]
]

matrix2 = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
sol = Solution(matrix2)
print(sol.longestIncreasingPath())
