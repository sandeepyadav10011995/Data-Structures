"""
Problem : Longest Sub-array with K Sum
Constraint : [Positives num only]
             [Positives/Negatives num only]

Subarray --> Contiguous part of the array

Brute Force: Generate all the subarray
            TC: O(N^3)  -- Cumulative Sum --> O(N^2)
            SC: O(N^2)

Better: Prefix Sum (Map) --> This will work for both Positive and Negative elements.
        TC: O(N)
        SC: O(N)

Optimal: Two Pointer --> Sliding Window Dynamic --> Works well for only arrays with Positive Values With/Without Zero
         TC: O(N) + O(N) --> O(2N)
         SC: O(1)

"""


class Solution:
    @staticmethod
    def longestSubArrayWithSumK1(nums: list[int], K: int) -> int:
        """
        Edge Case: When 0 is present in the array or duplicates are present nums = [2, 0, 0, 3], K = 3 ==> 3
        Solution: we don't need to override the first occurrence of the number
        """
        prefixSumMap = {}
        maxSubArrayLen = 0

        cumSum = 0
        for i in range(len(nums)):
            cumSum += nums[i]
            if cumSum == K:
                maxSubArrayLen = max(maxSubArrayLen, i+1)
            remSum = cumSum - K
            if remSum in prefixSumMap:
                maxSubArrayLen = max(maxSubArrayLen, i-prefixSumMap[remSum])
            if cumSum not in prefixSumMap:
                prefixSumMap[cumSum] = i

        return maxSubArrayLen

    @staticmethod
    def longestSubArrayWithSumK2(nums: list[int], K: int) -> int:
        maxSubArrayLen = 0
        windowStart = 0
        windowSum = 0

        for windowEnd in range(len(nums)):
            windowSum += nums[windowEnd]

            while windowSum > K:
                windowSum -= nums[windowStart]
                windowStart += 1

            if windowSum == K:
                maxSubArrayLen = max(maxSubArrayLen, windowEnd-windowStart+1)

        return maxSubArrayLen


sol = Solution()
print(sol.longestSubArrayWithSumK1(nums=[2, 0, 0, 3], K=3))
print(sol.longestSubArrayWithSumK2(nums=[2, 0, 0, 3], K=3))
