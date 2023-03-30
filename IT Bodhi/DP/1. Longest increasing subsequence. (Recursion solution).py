"""
Problem : Longest increasing subsequence. (Recursion solution)

"""


class Solution:
    def maxSequenceLength(self, arr: list[int], index: int, size: int) -> int:
        # Base Case
        if index >= size:
            return 0

        maxLength = 1
        for i in range(index+1, size):
            if arr[i] >= arr[index]:
                maxLength = max(self.maxSequenceLength(arr, i, size) + 1, maxLength)

        return maxLength

    def maxSequence(self, arr: list[int]) -> int:
        size = len(arr)
        maxLength = 0
        for i in range(size):
            maxLength = max(self.maxSequenceLength(arr, i, size), maxLength)

        return maxLength

    # Top-Down Approach Memoization
    def maxSequenceLengthTopDownMemo(self, arr: list[int], index: int, size: int, result: list[int]) -> int:
        # Base Case
        if index >= size:
            return 0

        if result[index] < 0:
            maxLength = 1
            for i in range(index + 1, size):
                if arr[i] >= arr[index]:
                    maxLength = max(self.maxSequenceLength(arr, i, size) + 1, maxLength)
                    result[i] = maxLength

        return result[index]

    # Bottom-Up Approach Memoization
    def maxSequenceLengthBottomUpMemo(self):

        pass


"""
Recursive Approach
TC: O(N^N) --> O(N!)
SC: O(N)

Top-Down Approach Memoization Approach
TC: O(N^2)
SC: O(N)

Bottom-Up Approach Memoization Approach
TC: O(N^2)
SC: O(N)


"""


class Solution2:
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


sol2 = Solution2()
print(sol2.longestIncreasingSubsequence(arr=[10, 1, 3, 4, 15, 6, 8, 20]))
