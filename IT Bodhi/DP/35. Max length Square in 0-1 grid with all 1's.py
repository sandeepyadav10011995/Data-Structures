"""
Problem : Max length Square in 0/1 grid with all 1's
Ex-: Input is a 2D array of 0/1 elements, then find the Max Square of max Length.

Approach 1:
F(i, j) =   0 if grid[i][j] == 0
            else:
                1 + min(F(i-1, j-1),
                      F(i-1, j),
                      F(, j-1))




------------- Max Sum ----------------------------------

Approach 1: Brute Force
Square-:
F(i, j, L) --> (i, j) --> Cell Top Left and length L
TC: O(N^3) * O(N^2) --> Checking at each cell --> O(N^5)

Rectangle-:
F(i, j, L, B) --> (i, j) --> Cell Top Left and length L and breadth B
TC: O(N^4) * O(N^2) --> Checking at each cell --> O(N^6)

    0   1   2   3   4   5   6   7   8   9
0
1
2
3
4            (RS,CS)*   *   *
5               *   *   *   *
6               *   *   *(RE,CE)
7
8
9

Approach-: Row wise Sum or Column Wise Sum
Square -:
TC: O(N^2) + O(N^3)
SC: O(N^2)
Sum of the square with RS,CS and RE,CE = Sum[RE][CE] -
                                         Sum[RS-1][CE] -
                                         Sum[RE][CS-1] +
                                         Sum[RS-1][CS-1]

Square -:
TC: O(N^2) + O(N^4)
SC: O(N^2)

"""


class Solution:
    def maxLengthSquare(self, grid, i, j):
        # Base Case:
        if i < 0 or j < 0:
            return 0
        if (i == 0 or j == 0) and grid[i][j] == 1:
            return 1

        return 1 + min(self.maxLengthSquare(grid, i-1, j-1),
                       self.maxLengthSquare(grid, i-1, j),
                       self.maxLengthSquare(grid, i, j-1))

    @staticmethod
    def maxLengthSquareDP(grid):
        N = len(grid)
        M = len(grid[0])
        mLengthSq = 0
        result = grid[:]
        for i in range(1, N):
            for j in range(1, M):
                if grid[i][j] == 0:
                    result[i][j] = 0
                else:
                    curLength = 1 + min(result[i-1][j-1],
                                           result[i-1][j],
                                           result[i][j-1])
                    result[i][j] = curLength
                    mLengthSq = max(mLengthSq, curLength)

        return mLengthSq
    """
    TC: O(N*M)
    SC: O(N*M)
    """


    @staticmethod
    def maxSquareSum(grid):
        N = len(grid)
        M = len(grid[0])
        maxSumSquareLength = 0
        for i in range(N):
            for j in range(M):
                for l in range(1, N-i+1):
                    # Assign rowStart,colStart and rowEnd,colEnd
                    rowStart, colStart = i, j
                    rowEnd, colEnd = i+l-1, j+l-1
                    # Check the sum Logic


        return maxSumSquareLength


sol = Solution()
matrix = [[1, 1, 1, 1],
        [0, 1, 1, 1],
        [1, 0, 1, 1],
        [1, 1, 1, 0]]
print(sol.maxLengthSquare(grid=matrix, i=3, j=3))
print(sol.maxLengthSquareDP(grid=matrix))


