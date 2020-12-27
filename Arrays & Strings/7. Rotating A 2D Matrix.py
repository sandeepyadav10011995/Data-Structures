class Solution:
    def _flipVertically(self, matrix):
        for top_row in range(0, len(matrix) // 2):
            bottom_row = len(matrix) - 1 - top_row
            matrix[top_row], matrix[bottom_row] = matrix[bottom_row], matrix[top_row]

    def _transposeMatrix(self, matrix):
        for row in range(0, len(matrix)):
            for col in range(row + 1, len(matrix[0])):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    def layer_rotate(self, matrix):
        size = len(matrix) - 1
        for layer in range(0, len(matrix)//2):
            for i in range(layer, size-layer):
                # Top Left --> Layer
                top_fence = matrix[layer][i]
                # Top Right --> Layer
                right_fence = matrix[i][size-layer]
                # Bottom Right --> Layer
                bottom_fence = matrix[size-layer][size-i]
                # Bottom Left --> Layer
                left_fence = matrix[size-i][layer]

                # Rotate the values by 90' --> Clockwise
                # Left Fence Value --> Top Fence
                matrix[layer][i] = left_fence
                # Top Fence Value --> Right Fence
                matrix[i][size-layer] = top_fence
                # Right Fence Value --> Bottom Fence
                matrix[size-layer][size-i] = right_fence
                # Bottom Fence Value --> Left Fence
                matrix[size-i][layer] = bottom_fence
        return matrix

    def flip_rotate(self, matrix):
        # Flip The Matrix Vertically
        self._flipVertically(matrix)
        # Transpose The Matrix
        self._transposeMatrix(matrix)
        return matrix


matric = [
  [ 1,  2,  3, 4],
  [ 5,  6,  7, 8],
  [ 9, 10, 11, 12],
  [13, 14, 15, 16]
]
matric2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
sol = Solution()
print(sol.layer_rotate(matric2))
# print(sol.flip_rotate(matric))
