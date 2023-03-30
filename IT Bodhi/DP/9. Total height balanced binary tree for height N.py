"""
Problem : Total height balanced binary tree for height N

F(N) = (N-1)*(N-1) (Equal elements on both sides) + (N-1)*(N-2) + (N-2)*(N-1)

"""


class Solution:
    def THBBT(self, N):
        # Base Case
        if N < 0:
            return 0
        if N == 0 or N == 1:
            return 1

        return self.THBBT(N-1)*self.THBBT(N-1) + 2*self.THBBT(N-1)*self.THBBT(N-2)

    """
    Branch = 3 and for every we have 2 ==> 6
    Level = N
    TC: O(6^N)
    SC: O(N)
    """

    def THBBTOptimized(self, N):
        # Base Case
        if N < 0:
            return 0
        if N == 0 or N == 1:
            return 1

        F_N_1 = self.THBBT(N-1)
        F_N_2 = self.THBBT(N-2)

        return F_N_1*F_N_1 + 2*F_N_1*F_N_2
    """
       Branch = 2
       Level = N
       TC: O(2^N)
       SC: O(N)
    """

    def THBBTOptimizedMemo(self, N, memo):
        # Base Case
        if N < 0:
            return 0
        if N == 0 or N == 1:
            return 1

        if memo[N] < 0:
            F_N_1 = self.THBBTOptimizedMemo(N - 1, memo)
            F_N_2 = self.THBBTOptimizedMemo(N - 2, memo)
            memo[N] = F_N_1*F_N_1 + 2*F_N_1*F_N_2

        return memo[N]

    """
    TC: 2*N
    SC: O(N)
    """
    @staticmethod
    def THBBTBottomUp(N):
        memo = [-1 for _ in range(N+1)]
        memo[0] = 1
        memo[1] = 1
        for n in range(2, N+1):
            memo[n] = memo[n-1]*memo[n-1] + 2*memo[n-1]*memo[n-2]

        return memo[-1]

    """
    Tc: O(N)
    SC: O(N)    
    """


sol = Solution()
print(sol.THBBT(N=5))
print(sol.THBBTOptimized(N=5))
print(sol.THBBTOptimizedMemo(N=5, memo=[-1 for _ in range(6)]))
print(sol.THBBTBottomUp(N=5))
