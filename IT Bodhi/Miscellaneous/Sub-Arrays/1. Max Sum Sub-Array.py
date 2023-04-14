"""
Problem : Maximum Sum sub-array in an integer array.
Subarray --> Contiguous part of the array

Approach 1: Brute Force: Generate all the subarray
            TC: O(N^3)  -- Cumulative Sum --> O(N^2)
            SC: O(N^2)

Approach 2: Cumulative Sum Approach.
        TC: O(N)
        O(1)


            2   -4   10  -6   5   -5  -7     3    8   -2     3   2   -10     -2
cumSum      2   -2   8    2   7    1  -6    -3    5    3     6   8    -2     -4
minSumFar   0   -2  -2   -2  -2
curSum      2   -2   6    0   4
maxSum      2    2   6    6   6


"""
import math


class SubArray:
    @staticmethod
    def maxSumSubArray(nums: list[int]) -> (list, int):
        N = len(nums)
        maxSum = -math.inf
        cumSum = 0
        minSumSoFar = 0
        start = 0
        end = 0

        for i in range(N):
            cumSum += nums[i]
            curSum = cumSum - minSumSoFar
            if cumSum < minSumSoFar:
                minSumSoFar = cumSum
                start = i+1
            if curSum > maxSum:
                maxSum = curSum
                end = i


        return nums[start:end+1], maxSum


sb = SubArray()
print(sb.maxSumSubArray(nums=[2, -4, 10, -6, 4, -5, -7, 3, 8, -2, 3, 2, -10, -2]))
