"""
Problem : Second-Largest Element In An Array

Brute Force -: Sort the array -> O(N*logN) + Largest(Last Element) --> O(1) + Second Largest(Iterate the array backwards) --> O(N)
               TC: O(N*logN + 1 + N) ~ O(N*logN)
               SC: O(N)

Better Solution: Largest(First Pass) + Second Largest(Second Pass)
                TC: O(N) + O(N) ~ O(2N)
                SC: O(1)

Optimal Solution: Two Pointer Approach
                  TC: O(N)
                  SC: O(1)
"""
import math


class Solution:
    @staticmethod
    def _secondLargest(nums: list[int], n: int) -> int:
        largest = nums[0]
        slargest = -math.inf

        for i in range(n):
            if nums[i] > largest:
                slargest = largest
                largest = nums[i]
            elif nums[i] != largest and nums[i] > slargest:
                slargest = nums[i]

        return -1 if slargest == -math.inf else slargest

    @staticmethod
    def _secondSmallest(nums: list[int], n: int) -> int:
        smallest = nums[0]
        ssmallest = math.inf

        for i in range(n):
            if nums[i] < smallest:
                ssmallest = smallest
                smallest = nums[i]
            elif nums[i] != smallest and nums[i] < ssmallest:
                ssmallest = nums[i]

        return -1 if ssmallest == math.inf else ssmallest

    def getSecondOrderElement(self, nums: list[int]) -> list[int, int]:
        n = len(nums)
        if n < 2:
            return [-1, -1]
        slargest = self._secondLargest(nums, n)
        ssmallest = self._secondSmallest(nums, n)
        return [slargest, ssmallest]
