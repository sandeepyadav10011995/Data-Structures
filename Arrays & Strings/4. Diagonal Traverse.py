"""
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

Example:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]
Note:
The total number of elements of the given matrix will not exceed 10,000.
"""


class Solution:
    def diagonalTraverse(self, matrix):
        # Check for empty matrices
        if not matrix or not matrix[0]:
            return []
        rows, cols = len(matrix), len(matrix[0])
        row = 0
        col = 0
        go_up = True
        output = []
        while 0 <= row < rows and 0 <= col < cols:
            output.append(matrix[row][col])

            if go_up:
                if row == 0 or col == cols-1: # terminating condition
                    if col == cols-1: # go down
                        row += 1
                    else:
                        col += 1
                    go_up = False
                else: # going up
                    row -= 1
                    col += 1
            else:
                if col == 0 or row == rows-1: # terminating condition
                    if row == rows-1: # go up
                        col += 1
                    else:
                        row += 1
                    go_up = True
                else: # going down
                    row += 1
                    col -= 1
        return output

mat = [
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]
]
sol = Solution()
print(sol.diagonalTraverse(mat))
