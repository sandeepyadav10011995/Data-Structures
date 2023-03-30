"""
Problem : Minimum notes needed to exchange currency

Variant 1: When Denominator is given and we unlimited supply fo all the denominators
F(N, denoms) = 1 + min(N-deno1,
                   N-deno2,
                   ...
                   )

Follow Up -: What if the denominator count is limited
Coins_Number : 3    2   2   1   1   2
Denominator  : 1    2   5   7   10  20

$1 coins count = 3
$2 coins count = 2
$5 coins count = 2
$7 coins count = 1
$10 coins count = 1
$20 coins count = 2

"""
import math


class SolutionVariant1:
    def minNotes(self, N, notes):
        # Base Case
        if N < 0:
            return math.inf
        if N == 0:
            return 0

        minVal = math.inf
        for i in range(len(notes)):
            minVal = min(minVal, 1 + self.minNotes(N-notes[i], notes))

        return minVal

    def minNotesMemo(self, N, notes, memo):  # Top-Down Approach
        # Base Case
        if N < 0:
            return math.inf
        if N == 0:
            return 0

        if memo[N] < 0:
            minVal = math.inf
            for i in range(len(notes)):
                minVal = min(minVal, 1 + self.minNotes(N - notes[i], notes))

            memo[N] = minVal
        return memo[N]

    @staticmethod
    def minNotesBottomUp(N, notes):
        memo = [N+1 for _ in range(N+1)]
        for amount in range(N+1):
            for denom in notes:
                if denom <= amount:
                    memo[amount] = min(memo[amount], 1+memo[amount-denom])

        return -1 if memo[-1] == N+1 else memo[-1]

    """
    TC: N*len(notes)
    SC: O(N)
    """
