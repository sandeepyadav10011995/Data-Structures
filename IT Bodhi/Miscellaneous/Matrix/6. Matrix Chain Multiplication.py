"""
Problem : Matrix chain multiplication
Ex-: A1, A2, A3, A4, A5
Ai : Ri, Ci
==> A1*(A2*A3)*(A4*A5) --> Min Cost


C(i, j) = for(k=i-->j-1) MIN(C(i, k) + C(k+1, j) + R(k)*R(k+1)*C(k+1))
Logic -: How to Split into Half with --> Min Cost

Ex -:   R   3   4   2   5   1   6
        C   4   2   5   1   6   3

TC: O(Summation(N))*N ~ O(N^3)
SC: O(N)

"""
import math


class Solution:
    MAX = math.inf

    def minMatrixChainMultiplicationCost(self, arrMatrix: list[list], start, end) -> int | float:
        # Base Case
        if start == end:  # Zero Cost because we have only one matrix
            return 0
        if start > end:
            return self.MAX

        minCost = self.MAX
        for i in range(start, end):
            minCost = min(minCost,
                          self.minMatrixChainMultiplicationCost(arrMatrix, start, i) +  # Left
                          self.minMatrixChainMultiplicationCost(arrMatrix, i+1, end) +  # Right
                          arrMatrix[0][start]*arrMatrix[1][i] * arrMatrix[1][end]  # Multiplication Cost:  --> S(r)*S(c)*E(c)
                          )

        return minCost

    @staticmethod
    def minMatrixChainMultiplicationCostBottomUp(arrMatrix) -> int:
        N = len(arrMatrix[0])
        # Fill the diagonal as 0 and rest as math.inf
        grid = [[math.inf if i != j else 0 for j in range(N)] for i in range(N)]
        """
                    0       1       2       3
                    4/2     2/3     3/8     8/3
        0    4/2     0      24      112     114  
        1    2/3     X       0      48      90 
        2    3/8     X       X       0      72
        2    8/3     X       X       X       0
        
        TC: 2*(N-1)*1 + 3(N-2)*2 + 4*(N-3)*3 + ... + N
           S = 1*(N-1) + 2(N-2) + 3(N-3) + ...
          2S = ...
                    ~ O(N^2/2)
        
        SC: O(N^2)
        """
        # Fill the DP table w.r.t Length wise
        for subArrLength in range(2, N+1):
            for i in range(N-subArrLength+1):
                minCost = math.inf
                for k in range(i, i+subArrLength-1):
                    minCost = min(minCost,
                                  grid[i][k] + grid[k+1][i+subArrLength-1] +
                                  arrMatrix[0][i]*arrMatrix[1][k]*arrMatrix[1][i+subArrLength-1])
                grid[i][i+subArrLength-1] = minCost

        return grid[0][N-1]


sol = Solution()
arr1 = [[2, 3, 4],
        [3, 4, 1]]
"""   
                            18
                           (0,2)                 
                18                     24    +     8
    (0,0) + (1,2) + 2*3*1           (0,1)   +       (2,2) + 2*4*1
      |        |(12)                   |               |
      0     (1,1)+(2,2)+ 3*4*1  (0,0)+(1,1)+2*3*4      0
              |      |            |      |
              0      0            0      0
 
"""

arr1 = [[2, 3, 4],
        [3, 4, 1]]
arr2 = [[3, 4, 2, 5, 1, 6],
       [4, 2, 5, 1, 6, 3]]
arr3 = [[4, 2,  3,  8],
        [2, 3,  8,  3]]
print(sol.minMatrixChainMultiplicationCost(arr1, 0, 2))
print(sol.minMatrixChainMultiplicationCost(arr2, 0, 5))
print(sol.minMatrixChainMultiplicationCostBottomUp(arr3))
