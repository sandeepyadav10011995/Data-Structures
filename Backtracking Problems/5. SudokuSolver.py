import math

class Solution:
    def __init__(self, board):
        self.board = board

    def _canPlaceValue(self, row, col, charToPlace):
        for place_row in self.board:
            if charToPlace == place_row[col]:
                return False
        for i in range(len(board[row])):
            if charToPlace == board[row][i]:
                return False
        regionSize = int(math.sqrt(len(self.board)))
        verticalBoxIndex = int(row / regionSize)
        horizontalBoxIndex = int(col / regionSize)
        topLeftOfSubBoxRow = int(regionSize * verticalBoxIndex)
        topLeftOfSubBoxCol = int(regionSize * horizontalBoxIndex)

        for i in range(int(regionSize)):
            for j in range(int(regionSize)):
                if charToPlace == self.board[topLeftOfSubBoxRow + i][topLeftOfSubBoxCol + j]:
                    return False
        return True

    def _canSolveSudokuFromCell(self, row, col):
        if col == len(self.board[row]):
            col = 0
            row += 1
            if row == len(self.board):
                return True
        if self.board[row][col] != '.':
            return self._canSolveSudokuFromCell(row, col+1)
        for val in range(1, len(self.board)+1):
            charToPlace = str(val)
            if self._canPlaceValue(row, col, charToPlace):
                self.board[row][col] = charToPlace
                if self._canSolveSudokuFromCell(row, col+1):
                    return True
                self.board[row][col] = '.'
        return False

    def solveSudoku(self):
        self._canSolveSudokuFromCell(0, 0)
        return self.board

board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
sol = Solution(board)
sol.solveSudoku()
print(sol.board)
