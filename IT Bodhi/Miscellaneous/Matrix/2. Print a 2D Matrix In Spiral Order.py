"""
Problem : Print a 2D integer array's elements in spiral order.
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""


class Solution:
    @staticmethod
    def spiralMatrix(matrix):
        if not matrix or not matrix[0]:
            return []

        output = []
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        while top <= bottom and left <= right:
            i = left
            # Left --> Right => Increment Top
            while i <= right:
                output.append(matrix[top][i])
                i += 1
            top += 1

            # Top --> Bottom => Decrement Right
            i = top
            while i <= bottom:
                output.append(matrix[i][right])
                i += 1
            right -= 1

            # Right --> Left => Decrement Bottom
            if top <= bottom:
                i = right
                while i >= left:
                    output.append(matrix[bottom][i])
                    i -= 1
                bottom -= 1
            # Bottom --> Top => Increment Left
            if left <= right:
                i = bottom
                while i >= top:
                    output.append(matrix[i][left])
                    i -= 1
                left += 1
        return output

mat = [[1,2,3],
        [4,5,6],
        [7,8,9]]
grid1 = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]


sol = Solution()
print(sol.spiralMatrix(mat))
print(sol.spiralMatrix(matrix=grid1))
