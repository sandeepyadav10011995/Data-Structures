"""
Problem : Find a value in a row-wise and column-wise sorted 2D array.
Dimensions: M*N
Approach 1: Considering the fact that the matrix is sorted w.r.t row wise
    Logic :: Use Binary --> logN
    TC: MlogN or NlogM
    SC: O(1)

Approach 2: Since the array is sorted w.r.t row and col wise both.
    Starting Point -: 1st row, Last col
    If the search value is smaller, then MOVE down and DISCARD the ROW
    If the search value is greater, then MOVE left and DISCARD the COL
    TC: O(M+N)
    SC: O(1)

"""

class Solution:
    @staticmethod
    def findValueInSorted2DMatrix(matrix: list[list[int]], K: int) -> list[int]:
        rowsSize = len(matrix)
        colSize = len(matrix[0])
        i = 0
        j = colSize-1
        while i < rowsSize and j >=0:
            if matrix[i][j] == K:
                return [i, j]
            elif matrix[i][j] < K:  # Discard the row and move down
                i += 1
            else:  # Discard the col and move left
                j -= 1

        return [-1, -1]


sol = Solution()
mat = [[1, 4, 8, 12, 15],
      [3, 5, 9, 16, 20],
      [7, 9, 11, 25, 27],
      [16, 22, 42, 62, 72]]
print(sol.findValueInSorted2DMatrix(matrix=mat, K=17))
print(sol.findValueInSorted2DMatrix(matrix=mat, K=16))
print(sol.findValueInSorted2DMatrix(matrix=mat, K=11))
print(sol.findValueInSorted2DMatrix(matrix=mat, K=80))
