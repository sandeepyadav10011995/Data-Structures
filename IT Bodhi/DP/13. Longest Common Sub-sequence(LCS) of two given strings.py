"""
Problem : Longest Common Sub-sequence(LCS) of two given strings
Make the bridges with no intersections.

Approach 1: Recursive
        LCS(i, j) = 1 + LCS(i+1, j-1) if s1[i] == s2[j]
                    max(LCS(i+1, j), LCS(i, j-1))

    TC: O(2^(M+N))
    SC: O(M+N) --> Call Stack

Approach 2: Top-Down --> Memo
    TC: O(2*M*N)
    SC: O(M*N)

Approach 2: Bottom Up
    TC: O(M*N)
    SC: O(M*N)
"""


class Solution:
    def lcsRecursive(self, s1, s2, i, j):
        # Base Case
        if i == -1 or j == -1:
            return 0

        if s1[i] == s2[j]:
            return 1 + self.lcsRecursive(s1, s2, i + 1, j - 1)

        return max(self.lcsRecursive(s1, s2, i - 1, j), self.lcsRecursive(s1, s2, i, j - 1))

    def lcsRecursiveMemo(self, s1, s2, i, j, memo):  # Top-Down Approach
        # Base Case
        if i < 0 or j < 0:
            return 0
        if memo[i][j] < 0:
            if s1[i] == s2[j]:
                memo[i][j] = 1 + self.lcsRecursive(s1, s2, i + 1, j - 1)
            else:
                memo[i][j] = max(self.lcsRecursive(s1, s2, i - 1, j), self.lcsRecursive(s1, s2, i, j - 1))
        return memo[i][j]

    @staticmethod
    def lcsBottomUp(s1, s2):
        M = len(s1)
        N = len(s2)

        memo = [[0] * (N + 1) for _ in range(M + 1)]

        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if s1[i - 1] == s2[j - 1]:
                    memo[i][j] = 1 + memo[i - 1][j - 1]
                else:
                    memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])

        return memo[-1][-1]


print("_" * 100)
sol = Solution()
print(sol.lcsRecursive(s1="ABCDT", s2="TACAD", i=4, j=4))
print(sol.lcsRecursiveMemo(s1="ABCDT", s2="TACAD", i=4, j=4, memo=[[-1] * (5)] * (5)))
print(sol.lcsBottomUp(s1="ABCDT", s2="TACAD"))
print("_" * 100)

"""
Follow Up : Return the sequence for the LCS
"""


class Solution2:
    @staticmethod
    def lcsBottomUp(s1, s2):
        M = len(s1)
        N = len(s2)

        memo = [[0] * (N + 1) for _ in range(M + 1)]

        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if s1[i - 1] == s2[j - 1]:
                    memo[i][j] = 1 + memo[i - 1][j - 1]
                else:
                    memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])

        sequence = []
        i, j = M, N
        while i > 0 and j > 0 and memo[i][j] > 0:
            if s1[i - 1] == s2[j - 1]:
                sequence.append(s1[i - 1])
                i -= 1
                j -= 1
            else:
                if memo[i - 1][j] > memo[i][j - 1]:
                    i -= 1
                else:
                    j -= 1
        return "".join(reversed(sequence))


sol2 = Solution2()
print(sol2.lcsBottomUp(s1="ABCDT", s2="TACAD"))
print(sol2.lcsBottomUp(s1="AGGTAB", s2="GXTXAYB"))
print("_" * 100)

"""
Follow Up : Return all the sequences for the LCS
"""


class Solution3:
    @staticmethod
    def addCharToLOLR(lolr, s):
        for l in lolr:
            l.append(s)

    @staticmethod
    def mergeLOLR(lolr1, lolr2):
        lolr1.extend(lolr2)

    def generateAllSequences(self, s1, s2, memo, i, j):
        rt = [[]]
        # Base Case
        if i <= 0 or j <= 0 or memo[i][j] <= 0:
            return rt

        if s1[i - 1] == s2[j - 1]:
            lolr = self.generateAllSequences(s1, s2, memo, i - 1, j - 1)
            self.addCharToLOLR(lolr, s1[i - 1])
            return lolr
        else:
            if memo[i - 1][j] == memo[i][j - 1]:
                lolr1 = self.generateAllSequences(s1, s2, memo, i - 1, j)
                lolr2 = self.generateAllSequences(s1, s2, memo, i, j - 1)
                self.mergeLOLR(lolr1, lolr2)
                return lolr1
            elif memo[i - 1][j] > memo[i][j - 1]:
                lolr1 = self.generateAllSequences(s1, s2, memo, i - 1, j)
                return lolr1
            else:
                lolr2 = self.generateAllSequences(s1, s2, memo, i, j - 1)
                return lolr2

    def lcsBottomUp(self, s1, s2):
        M = len(s1)
        N = len(s2)

        memo = [[0] * (N + 1) for _ in range(M + 1)]

        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if s1[i - 1] == s2[j - 1]:
                    memo[i][j] = 1 + memo[i - 1][j - 1]
                else:
                    memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])
        allSequences = self.generateAllSequences(s1, s2, memo, M, N)
        return allSequences


sol3 = Solution3()
print(sol3.lcsBottomUp(s1="ABCDT", s2="TACAD"))
print(sol3.lcsBottomUp(s1="AGGTAB", s2="GXTXAYB"))
print("_"*100)
