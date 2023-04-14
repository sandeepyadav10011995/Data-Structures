"""
Problem : Split N numbers in 2 groups having same average.

Ex -: arr = [2, 3, 4, 5, 2, 2];  Avg = sum(arr)/N
(0, K), (K+1, N-1) Two groups with avg = Avg

Mathematical Property : If avg of A subarray == avg of B subarray == X
                        Then avg of (A+B) == X

Approach : DP --> 3D DP

"""
import math


class Solution:
    def _fillGrid(self, grid, arr, index, size, arrSum):
        # Base Case
        if index == size:
            return

        for i in range(size):
            for j in range(arrSum):
                if grid[i][j] == 1:
                   if j + arr[index] <= arrSum and grid[i+1][j+arr[index]] == 0:
                       grid[i+1][j+arr[index]] = -1
            self.fillAllOnes(grid)


        self._fillGrid(grid, arr, index + 1, size, arrSum)

    def splitArrayIn2GroupsWithAvgAsAvg(self, arr):
        size = len(arr)
        arrSum = sum(arr)
        grid = [[math.inf for _ in range(arrSum)] for _ in range(size)]

        self._fillGrid(grid, arr, index=0, size=size, arrSum=arrSum)
        return grid[-1][-1]


sol = Solution()
array = [2, 3, 4, 5, 2, 2]
print(sol.splitArrayIn2GroupsWithAvgAsAvg(array))
