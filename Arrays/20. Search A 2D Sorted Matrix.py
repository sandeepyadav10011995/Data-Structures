"""
Given a 2D matrix (which is m x n) find the given element with value value. If the matrix contains the value return true, otherwise return false.

Variant 1:
In this variant, all values in the matrix are increasing in row-major order.

This means that:
Each row is sorted
The last element in row i is <= the first element in row i+1
By virtue of the previous two properties, the columns are sorted

Example:
Input:
value = 6
[
  [0, 1, 2, 3],
  [4, 5, 6, 7],
  [8, 9, 10, 11]
]

Output: true

Variant 2:
In this variant:
Each row is sorted
Each column is sorted
There is no guarantee that the last element in row i is <= the first element in row i+1

Example:
Input:
value = 20
[
  [1, 4, 7, 11]
  [8, 9, 10, 20]
  [11, 12, 17, 30]
]

Output: true

Constraints:
arr[i] >= 0
All elements of the matrix are unique
"""

class Solution:
    def variant1(self, matrix, value):
        rows = len(matrix)
        # Edge Case
        if rows == 0:
            return False
        cols = len(matrix[0])
        left = 0
        right = rows * cols - 1

        while left <= right:
            mid = left + ((right-left)//2)
            mid_row = mid // cols
            mid_col = mid % cols

            mid_val = matrix[mid_row][mid_col]
            if mid_val == value:
                return True
            elif mid_val < value:
                left = mid + 1
            else:
                right = mid - 1
        return False

    def variant2(self, matrix, value):
        if not matrix:
            return False
        # LD or RU Approach --> LD
        rows = len(matrix)
        cols = len(matrix[0])
        row = 0
        col = cols - 1
        while col >= 0 and row < rows:
            """
                Cases:
                    1.
                    2.
                    3.
            """
            if matrix[row][col] == value:
                return True
            elif matrix[row][col] < value:
                row += 1
            elif matrix[row][col] > value:
                col -= 1
        return False


value = 13
mat = [
  [0, 1, 2, 3],
  [4, 5, 6, 7],
  [8, 9, 10, 11]
]

mat2 = [
  [1, 4, 7, 11],
  [8, 9, 10, 20],
  [11, 12, 17, 30]
]


sol = Solution()
print(sol.variant1(mat, value))
print(sol.variant2(mat2, value))
