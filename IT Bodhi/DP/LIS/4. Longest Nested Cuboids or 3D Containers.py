"""
Problem : Longest nested cuboids/ 3d containers

Question: When the problem is about 3D
Height      5   6   3   1   2   8   7
Length      6   8   4   8   1   7   10
Breadth     8   9   4   2   1   5   5

Sort according to Height-:
Height      1   2   3   5   6   7   8
Length      8   1   4   6   8   10  7
Breadth     2   1   4   8   9   5   5
Then apply LIS combined on Length and Breadth together
LIS         1   1   2   3   4   3   3

maxLIS = 4

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
    def maxCuboidsLIS(cuboids: list) -> int:
        N = len(cuboids)
        maxCuboidLIS = [1 for _ in range(N)]
        cuboids.sort(key=lambda x: x[0])

        maxCuboidStack = 0
        for i in range(1, N):
            for j in range(i):
                # Perform LIS combined on other two dimensions
                if cuboids[i][1] > cuboids[j][1] and cuboids[i][2] > cuboids[j][2] and maxCuboidLIS[i] < maxCuboidLIS[j] + 1:
                    maxCuboidLIS[i] = maxCuboidLIS[j] + 1
            maxCuboidStack = max(maxCuboidStack, maxCuboidLIS[i])

        return maxCuboidStack


cuboids = [(5, 6, 8), (6, 8, 9), (3, 4, 4), (1, 8, 2), (2, 1, 1), (8, 7, 5), (7, 10, 5)]
sol = Solution()
print(sol.maxCuboidsLIS(cuboids))
