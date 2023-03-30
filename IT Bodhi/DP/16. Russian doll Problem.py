"""
Problem : Russian Doll Problem
Doll 1 >>>> Doll 2 >>> Doll 3 >> Doll 4 > Doll 5
L1, R1      L2, R2     L3, R3    L4, R4   L5, R5
D1          D2         D3        D4       D5

Condition : For D1 and D2 ==> R2 < R1 and L2 < L1
Dolls = [(4, 6), (8, 8), (3, 10), (6, 5), (4, 4), (6, 2), (2, 2)]

One Valid Solution is -: R2->R1->R5->R7 = 4

Approach 1: LIS in 2D
            Therefore we need to sort it w.r.t either Length or Breadth.
            If two values are equal then sort that w.r.t other parameter
            ==> 2   3   4   4   6   6   8   10
                2   10  4   6   2   5   8   4

        LIS-:   1   2   2   3   2   3   4   3

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

    def maxCuboids(self, cuboids):
        cuboids.sort()
        print(cuboids)

        


cuboids = [
    [5, 6, 3, 1, 2, 8, 7],
    [8, 1, 4, 6, 8, 10, 7],
    [2, 1, 4, 8, 9, 5, 5]
]

[[2, 1, 4, 8, 9, 5, 5],
 [5, 6, 3, 1, 2, 8, 7],
 [8, 1, 4, 6, 8, 10, 7]]
print(cuboids)
cuboids.sort(key=lambda x: x[:])
print(cuboids)
