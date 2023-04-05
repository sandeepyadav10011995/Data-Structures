"""
Problem : Rotate a N*N square integer matrix to 90 degree clockwise.

Concept -: i, j -: i --> row, j--> col
So we see that on rotation col is becoming new row. and col = N-i-1

Therefore;
        N = 4
        (i, j) ====> (j, N-i-1)
        (3, 2) ====> (2, 0)

Approach 1: Flip the matrix(across rows) Then take a transpose of it.
Downside : Two-many swaps
TC: O(N^2)
SC: O(1)

Approach 2: Layer By Layer
Good-side-: Shifting
Note-: Shifting < Swapping (Costs)
TC: O(N^2)
SC: O(1)

"""


class Rotate:
    @property
    def _abc(self):
        pass

    @staticmethod
    def _flipMatrixVertically(matrix: list[list[int]]) -> None:
        rows = len(matrix)
        for top in range(rows//2):
            bottom = rows-top-1
            # Flip the rows
            matrix[top], matrix[bottom] = matrix[bottom], matrix[top]

    @staticmethod
    def _transpose(matrix: list[list[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        for row in range(rows):
            for col in range(row+1, cols):
                upperTriangle = matrix[row][col]
                lowerTriangle = matrix[col][row]
                # Swap the two indexes values
                matrix[row][col] = lowerTriangle
                matrix[col][row] = upperTriangle

    def matrixRotateUsingFlipLogic(self, matrix: list[list[int]]) -> list[list[int]]:
        self._flipMatrixVertically(matrix)
        self._transpose(matrix)
        return matrix

    @staticmethod
    def matrixRotateUsingLayerByLayerLogic(matrix):
        size = len(matrix) - 1

        for layer in range(size+1//2):
            for i in range(layer, size-layer):
                # Starts at the top left of layer
                topFence = matrix[layer][i]
                # Starts at the top right of layer
                rightFence = matrix[i][size-layer]
                # Starts at the bottom right of the layer
                bottomFence = matrix[size-layer][size-i]
                # Starts at the bottom left of the layer
                leftFence = matrix[size-i][layer]

                # Rotate 90 Degree clockwise element by element
                # Start walking top fence
                matrix[layer][i] = leftFence
                # Start walking right fence
                matrix[i][size-layer] = topFence
                # Start walking bottom fence
                matrix[size-layer][size-i] = rightFence
                # Start walking left fence
                matrix[size-i][layer] = bottomFence
        return matrix


rotate = Rotate()
grid1 = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]
grid2 = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]

rotate.
print(rotate.matrixRotateUsingFlipLogic(matrix=grid1))
print(rotate.matrixRotateUsingLayerByLayerLogic(matrix=grid2))
