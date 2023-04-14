"""
==================  KADANE's ALGORITHM =======================
globalMax, localMax
Update when globalMax with localMax

Problem : Max sum sub-matrix in a given 2D integer matrix.
Brute Force Approach -:
    - No of top-left corners = rows*cols
    - Therefore, a particular top-left corner, all the possible bottom right corners, we are going to try = rows*cols
    => TC: O(rows^2*cols^2)
Note: This can be improved by Kadane's Algorithm !!

"""
import math
from dataclasses import dataclass


class KadaneAlgorithm:
    @staticmethod
    def _kadane(nums: list[int]) -> (int, int, int):
        N = len(nums)
        gmax = -math.inf
        lmax = 0
        start = 0
        end = 0
        subStart = 0

        for i in range(N):
            lmax += nums[i]
            if gmax < lmax:
                gmax = lmax
                start = subStart
                end = i

            if lmax < 0:
                lmax = 0
                subStart = i+1

        return gmax, start, end

@dataclass
class KadaneResult:
    maxSumSoFar: int
    startIndex: int
    endIndex: int

@dataclass
class SubMatrix:
    maxSum: int = 0
    leftBorderIndex: int = 0
    rightBorderIndex: int = 0
    topBorderIndex: int = 0
    bottomBorderIndex: int = 0


class Matrix:
    @staticmethod
    def kadaneResult(nums) -> KadaneResult:
        maxSumSoFar = 0
        maxStartIndex = 0
        maxEndIndex = 0
        curStart = 0
        runningMax = 0

        for i in range(len(nums)):
            runningMax += nums[i]
            if runningMax < maxSumSoFar:
                runningMax = 0
                curStart = i+1

            if runningMax > maxSumSoFar:
                maxSumSoFar = runningMax
                maxStartIndex = curStart
                maxEndIndex = i

        return KadaneResult(maxSumSoFar=maxSumSoFar, startIndex=maxStartIndex, endIndex=maxEndIndex)

    def maxSumSubMatrix(self, matrix) -> SubMatrix:
        rows = len(matrix)
        cols = len(matrix[0])
        maxSumSubMatrix = SubMatrix()
        for left in range(cols):
            runningRowsSum = [0] * rows
            for right in range(rows):
                for i in range(rows):
                    runningRowsSum[i] += matrix[i][right]
                kadaneResult = self.kadaneResult(runningRowsSum)
                if kadaneResult.maxSumSoFar > maxSumSubMatrix.maxSum:
                    maxSumSubMatrix.maxSum = kadaneResult.maxSumSoFar
                    maxSumSubMatrix.leftBorderIndex = left
                    maxSumSubMatrix.rightBorderIndex = right
                    maxSumSubMatrix.topBorderIndex = kadaneResult.startIndex
                    maxSumSubMatrix.bottomBorderIndex = kadaneResult.endIndex

        return maxSumSubMatrix
