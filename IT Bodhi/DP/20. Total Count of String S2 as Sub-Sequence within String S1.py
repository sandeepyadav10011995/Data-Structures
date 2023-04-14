"""
Problem : Total count of string s2 as sub-sequence within string s1
Definition of SubSequence -: A contiguous/non-contiguous sequence which follows the order.
Ex -: arr = [3, 1, 2]
     Total SubSequences of arr = [ [], [3], [1], [2], [3, 1], [1, 2], [3, 2], [3, 1, 2]]

Example -: Inputs
s1 = acbabbcbc --> L1
s2 = abc       --> L2

Approach 1: Brute Force
            Total combinations -: L1 C L2
Approach 2:

    "   a   a   b   c   b   c
"   1   1   1   1   1   1   1
a   0   1   2   2   2   2   2
b   0   0   0   2   2   4   4
c   0   0   0   0   2   2   6

F(i, j) = if s1[i] != s2[j] --> F(i-1, j)
         else: F(i, j-1) + F(i-1, j-1)

"""

class Solution:
    def totalSuSequenceCount(self, s1, s2, i, j):
        # Base Case
        pass

    @staticmethod
    def totalSuSequenceCountBottomUp(s1, s2):
        N = len(s2)
        M = len(s1)

        grid = [[0 for _ in range(M+1)] for _ in range(N+1)]

        # Fill the first row as "" with 1
        for i in range(M+1):
            grid[0][i] = 1

        for i in range(1, N+1):
            for j in range(1, M+1):
                if s2[i-1] == s1[j-1]:
                    grid[i][j] = grid[i][j-1] + grid[i-1][j-1]
                else:
                    grid[i][j] = grid[i][j-1]

        return grid[-1][-1]

sol = Solution()
s1 = "aabcbc"
s2 = "abc"
print(sol.totalSuSequenceCountBottomUp(s1, s2))


