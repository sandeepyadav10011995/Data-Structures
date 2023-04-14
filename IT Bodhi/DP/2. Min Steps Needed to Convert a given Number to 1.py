"""
Problem : Minimum steps needed to convert a given number integer to 1.


N  --> N/2 if even
   --> N/3 if divisible by 3
   --> N-1

F(N) = min(F(N/2), F(N/3), F(N-1))

"""
import math


class Solution:
    def minStepsRecursive(self, N):
        # Base Case
        if N == 1:
            return 1

        divBy2 = self.minStepsRecursive(N//2) if N % 2 == 0 else math.inf
        divBy3 = self.minStepsRecursive(N//3) if N % 3 == 0 else math.inf
        subBy1 = self.minStepsRecursive(N-1)

        return 1 + min(divBy2, divBy3, subBy1)

    """
    TC: O(3^N)
    SC: O(N) --> Call Stack
    """

    def minStepsMemo(self, N, memo):  # Top-Down Approach
        # Base Case
        if N == 1:
            return 1

        if memo[N] < 0:
            divBy2 = self.minStepsRecursive(N // 2) if N % 2 == 0 else math.inf
            divBy3 = self.minStepsRecursive(N // 3) if N % 3 == 0 else math.inf
            subBy1 = self.minStepsRecursive(N - 1)
            memo[N] = 1 + min(divBy2, divBy3, subBy1)

        return memo[N]
    """
    Level = N
    Branch = 1
    TC: 3N 
    SC: O(N) --> Space for the memo
    """
    @staticmethod
    def minStepsMemoBottomUp(N):  # Bottom-Up Approach
        memo = [-1 for _ in range(N+1)]
        memo[0] = 1

        for i in range(1, N+1):
            for j in range(3):
                if j == 0 and i % 2 == 0:
                    memo[i] = min(memo[i], 1+memo[i//2])
                elif j == 1 and i % 3 == 0:
                    memo[i] = min(memo[i], 1+memo[i//3])
                else:
                    memo[i] = min(memo[i], 1+memo[i-1])

        return -1 if memo[-1] < 0 else memo[-1]


"""
TC: O(3*N) ~ O(N)
SC: O(N)
"""
