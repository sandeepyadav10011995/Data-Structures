"""
Problem : Max sum increasing subsequence
Ex-: 10, 1, 3, 4, 15, 6, 8, 20 ==> (1, 3, 4, 6, 8, 20) = 42, (10, 15, 20) = 45
"""


class Solution:
    @staticmethod
    def longestIncreasingSubsequence(arr):
        N = len(arr)
        lis = [1 for _ in range(N)]

        for i in range(1, N):  # O(N^2)
            for j in range(i):
                if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                    lis[i] = lis[j] + 1

        maxLength = 0
        for i in range(N):
            maxLength = max(maxLength, lis[i])

        return maxLength
    """
    TC: O(N^2)
    SC: O(N)
    """

    @staticmethod
    def maxSumLongestIncreasingSubsequence(arr):
        N = len(arr)
        maxSum = 0
        maxSumLIS = [0 for _ in range(N)]
        # Fill the values for all the indexes
        for i in range(N):
            maxSumLIS[i] = arr[i]

        for i in range(1, N):
            for j in range(i):
                if arr[i] > arr[j] and maxSumLIS[i] < maxSumLIS[j] + arr[i]:
                    maxSumLIS[i] = maxSumLIS[j] + arr[i]

        for i in range(N):
            maxSum = max(maxSum, maxSumLIS[i])

        return maxSum
    """
    TC: O(N^2)
    SC: O(N)
    """


sol = Solution()
print(sol.longestIncreasingSubsequence(arr=[10, 1, 3, 4, 15, 6, 8, 20]))
print(sol.maxSumLongestIncreasingSubsequence(arr=[10, 1, 3, 4, 15, 6, 8, 20]))
