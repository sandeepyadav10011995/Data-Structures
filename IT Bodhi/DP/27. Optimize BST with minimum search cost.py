"""
Problem : Optimize BST with minimum search cost.
Ex-:                      20
                    8           25
               1       15           40
                 5

Search for 5 --> 4 Comparisons will be done  ==>
Search for 40 --> 3 Comparisons will be done ==>

Minimize the Cost of all the elements search
Element:    1   5   8   15  20  25  40
Frequency:  100 5   25  5   10  15  10
Minimize   (C1  C2  C3  C4  C5  C6  C7)

Approach 1: Put the element as root with max Frequency (Greedy approach)
        Problem : Does Not Guarantee the best result

Approach 2: MinCost(i, j) = MinCost(i, K-1) + SumOfFreq(i, K-1) + MinCost(K+1, j) + SumOfFreq(K+1, j) + arr[1][K]
Ideally the cost of K index = LeftTree Cost + RightTree Cost + Freq(K)
But since the root is coming down 1 level in both the tree, therefore the cost will be as level is getting increased by one each
Ex-: 5-10 --> 10                                5
     8-20 --> 2*40;  Total Cost = 50                8

Suppose now 3 is the root now               3
                                        5
                                            8

Therefore, new Total Cost = 2*10 + 3*20  = 80
Therefore, for one level down, new Total Cost = 3*10 + 4*20  = 110
Pattern ==> 50-->80-->110-->140 i.e, diff*(3*level-1)
Diff = |Freq Diff| = |10-20| = 10
Level = 1 ==> Cost = 50
Level = 2 ==> PrevLevel Cost + 3*(Level-1)*Diff = 50 + 3*1*10 = 80
Level = 3 ==> 1st Level Cost + 3*(Level-1)*Diff = 50 + 3*2*10 = 110
Level = 4 ==> 1st Level Cost + 3*(Level-1)*Diff = 50 + 3*3*10 = 140


Cost(i, j) = for k in range(i, j) Min(Cost(i, k-1) + Sum(i, k-1) +
                                      Cost(k+1, j) + Sum(k=1, j) +
                                      arr[k])

 1   5   8   15  20  25  40
 100 5   25  5   10  15  10

TC: O(N^3)
SC: O(N^2)
"""
import math
from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    val: int = None
    left: Any = None
    right: Any = None

@dataclass
class ReturnType:
    root: Any = None
    minCost: float = math.inf

class Solution:
    MAX = math.inf
    def minCost(self, arr, i, j) -> int:
        # Base Case
        if i > j:
            return 0
        if i == j:
            return arr[1][i]
        mCost = self.MAX
        for k in range(i, j):
            mCost = min(mCost,
                          self.minCost(arr, i, k) + sum(arr[1][i:k]) +
                          self.minCost(arr, k+1, j) + sum(arr[1][k+1:j+1]) +
                          arr[1][k]
                          )
        return mCost
    """
    TC: O(2^(N^2)*N)
    SC: O(N^2) + O(N^2) 
    """

    def minCostOptimized(self, arr, i, j) -> ReturnType:
        returnType = ReturnType()
        # Base Case
        if i > j:
            returnType.minCost = 0
            return returnType
        if i == j:
            returnType.root = arr[0][i]
            returnType.minCost = arr[1][i]
            return returnType
        mCost = self.MAX
        leftBT, rightBT, index = Node(), Node(), None
        for k in range(i, j):
            LV = self.minCostOptimized(arr, i, k)
            RV = self.minCostOptimized(arr, k+1, j)
            val = LV.minCost + RV.minCost + sum(arr[1][i:k]) + sum(arr[1][k+1:j+1]) + arr[1][k]
            if val < mCost:
                leftBT = LV.root
                rightBT = RV.root
                mCost = val
                index = k

        node = Node()
        node.val = arr[0][index]
        node.left = leftBT
        node.right = rightBT

        returnType.root = node
        returnType.minCost = mCost
        return returnType
    """
    TC: O(N^3)
    SC: O(N^2) + O(N^2) ~ O(N^2) 
    """

    @staticmethod
    def minCostBottomUp(arr):
        N = len(arr[0])
        grid = [[arr[1][j] if i==j else math.inf for j in range(N)] for i in range(N)]

        # Fill the Table Length wise
        for size in range(2, N+1):
            for i in range(N-size+1):
                minCost = math.inf
                j = i+size-1
                for k in range(i, j):
                    minCost = min(minCost,
                                  grid[i][k] + sum(arr[1][i:k]) +
                                  grid[k+1][j] + sum(arr[1][k+1:j+1]) +
                                  arr[1][k]
                                  )
                grid[i][j] = minCost

        return grid[0][-1]
    """
    TC: O(N^3)
    SC: O(N^2) 
    """


sol = Solution()
array1 = [[1, 5, 8, 15, 20, 25, 40],
         [100, 5, 25, 5, 10, 15, 10]]
print(sol.minCost(array1, 0, 6))
rt1 = sol.minCostOptimized(array1, 0, 6)
print(rt1.minCost)
print(rt1.root.val)
print(sol.minCostBottomUp(array1))
print("*"*100)
array2 = [[5, 8, 10, 15, 20],
         [10, 20, 15, 25, 3]]
print(sol.minCost(array2, 0, 4))
rt2 = sol.minCostOptimized(array2, 0, 4)
print(rt2.minCost)
print(rt2.root.val)
print(sol.minCostBottomUp(array2))
