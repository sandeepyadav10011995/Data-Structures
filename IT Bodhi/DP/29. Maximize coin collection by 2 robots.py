"""
Problem : Maximize coin collection by 2 robots

A robot at (i, j) can move in three directions i.e, (i+1, j-1)-->Left Diagonal,
                                                    (i+1, j) --> Down,
                                                    (i+1, j+1) --> Right Diagonal

We are given two starting points, (0, i), (0, j)
i --> Robot 1 => (0, i)
j --> Robot 2 => (0, j)

MaxCombinedCoins(i, j) =
"""
import math


class Solution:
    def __init__(self):
        self.MIN = -math.inf

    def _maxCombinedCoinsUtil(self, grid, rows, cols, i, j, row):
        # Base Case
        if i < 0 or j < 0 or i >= rows or j >= cols:
            return self.MIN

        if row == 0 and i != 0 and j != cols-1:
            return self.MIN

        maxCost = self.MIN
        for p in range(i-1, i+2):
            for q in range(j-1, j+2):
                maxCost = max(maxCost,
                              self._maxCombinedCoinsUtil(grid, p, q, row - 1))
        totalCost = maxCost + (grid[row][i] if i==j else grid[row][i] + grid[row][j])

        return totalCost

    def maxCombinedCoins(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):




"""
VISIT AGAIN !!

"""
