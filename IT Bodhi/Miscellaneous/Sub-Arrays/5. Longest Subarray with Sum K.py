"""
Longest Sub-Array with Sum K

Approach 1: Brute Force
            TC: O(N^

Approach 2: PrefixSum Map
            TC: O(N)
            SC: O(N)

"""


class Solution:
    @staticmethod
    def maxLenSubArray(nums: list[int]) -> int:
        N = len(nums)
        prefixSum = {}
        maxLength = 0
        cumSum = 0
        for i in range(N):
            cumSum += nums[i]
            if cumSum == 0:
                maxLength = i+1
            else:
                if cumSum in prefixSum:
                    maxLength = max(maxLength, i-prefixSum.get(cumSum))
                else:
                    prefixSum[cumSum] = i

        return maxLength
