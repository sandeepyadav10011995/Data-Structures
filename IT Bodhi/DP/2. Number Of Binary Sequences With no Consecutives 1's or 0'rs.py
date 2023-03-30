"""
Problem : Given a positive integer N, count all possible distinct binary strings of length N such that there are no
          consecutive 1’s.
Eg -:

Input:  N = 2
Output: 3
// The 3 strings are 00, 01, 10

Input: N = 3
Output: 5
// The 5 strings are 000, 001, 010, 100, 101

We'll use recursion first and if the last digit was '0' we have 2 options -> append '0' to it or append '1' to it
else if the last digit is '1' we can only append '0' to it since consequtive 1's are not allowed

"""


class Solution:
    def solveRecursive(self, prev: int, n: int) -> int:
        # Base Case
        if n == 0:
            return 0
        if n == 1:  # We have two options i.e 0 and 1
            return 2 if prev == 0 else 1

        if prev == 0:  # We have two options i.e 0 and 1
            return self.solveRecursive(0, n-1) + self.solveRecursive(1, n-1)

        if prev == 1:  # We have only one option i.e 0
            return self.solveRecursive(0, n-1)

    @staticmethod
    def solveDP1(n: int):
        dp = [[0 for _ in range(2)] for _ in range(n+1)]
        # Fill the Base Values
        dp[0][0] = 1
        dp[0][1] = 0

        for i in range(1, n+1):
            for j in range(2):
                if j == 0:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j+1]
                else:
                    dp[i][j] = dp[i-1][j-1]

        return sum(dp[-1])

    @staticmethod
    def solveDP2(n: int):
        zeros = [0 for _ in range(n+1)]
        ones = [0 for _ in range(n + 1)]

        # Fill the base Values
        zeros[0] = ones[0] = 0
        zeros[1] = ones[1] = 1

        for i in range(2, n+1):
            zeros[i] = zeros[i-1] + ones[i-1]
            ones[i] = zeros[i-1]

        return zeros[-1] + ones[-1]


sol = Solution()
print(sol.solveDP1(3))
print(sol.solveDP2(3))


"""
Follow Up -: 0, 1, 2 -> No consecutive i.e, no two 0 or no two 1 or no two 2 can be together
K = 3
F(1) = 3 * 2^0 = 3 * 1 = 3
F(2) = 3 * 2^(1) = 3 * 2 = 6
F(3) = 3 * 2^(2) = 3 * 2 * 2 = 12
F(4) = 3 * 2^(3) = 3 * 2 * 2 * 2 = 24 
Therefore F(N) = K * (K-1)^(N-1)

"""
