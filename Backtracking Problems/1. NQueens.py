class Solution:
    results = []
    count = 0
    def _isValid(self, col_placement):
        row_id = len(col_placement) - 1
        for j in range(0, row_id):
            diff = abs(col_placement[j]-col_placement[row_id])
            if diff == 0 or diff == (row_id-j):
                return False
        return True

    def _solveNQueens(self, n, row, col_placement=[]):
        if row == n:
            self.results.append(col_placement[:])
            self.count += 1
        else:
            for col in range(0, n):
                col_placement.append(col)
                if self._isValid(col_placement):
                    self._solveNQueens(n, row+1, col_placement)
                col_placement.pop()

    def totalNQueens(self, n):
        self._solveNQueens(n, 0)
        return self.results

sol = Solution()
sol.totalNQueens(4)
print(sol.results)
print(sol.count)
