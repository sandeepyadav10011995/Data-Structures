"""
Problem : Minimum notes to make sum k

Variant 2: What if we are given an array of denominators.
F(N, i) = 0 if F(N, i) if N == 0
          MAX if F(N, i) if N < 0
          MAX if i < 0
          min(F(N, i-1), F(N-arr[i], i-1)) --> Otherwise min(choose i, Do not choose i)

N : Total Amount
i : index of the array :: Start Point = End Index of the Array

TC: O(2^size) : size --> array size
SC: O(size) --> Call Stack

"""
import math


class SolutionVariant2:
    def __init__(self):
        self.MAX = math.inf

    def minNotes(self, N, arr, index):
        # Base Case
        if N == 0:
            return 0
        if N < 0:
            return self.MAX
        if index < 0:
            return self.MAX

        return min(self.minNotes(N, arr, index-1), 1 + self.minNotes(N-arr[index], arr, index-1))
    """
    TC: O(2^size) : size --> array size
    SC: O(size) --> Call Stack
    """
    def minNotesMemo(self, N, arr, index, memo):  # Top-Down Approach
        # Base Case
        if N == 0:
            return 0
        if N < 0:
            return self.MAX
        if index < 0:
            return self.MAX
        if memo[N] == self.MAX:
            memo[N] = min(self.minNotes(N, arr, index - 1), 1 + self.minNotes(N - arr[index], arr, index - 1))

        return memo[N]

    """
        TC: O(2*Size*N)
        SC: O(N)
    """

    def minNotesBottomUp(self, N, arr):
        size = len(arr)
        memo = [[self.MAX for _ in range(N+1)] for _ in range(size+1)]
        # Fill the memo table for 0 amount as 0 notes
        for i in range(size):
            memo[i][0] = 0

        for i in range(1, size+1):
            for j in range(1, N+1):
                # Handling j-arr[i-1] is very important
                if j >= arr[i-1]:
                    memo[i][j] = min(memo[i-1][j], 1+memo[i-1][j-arr[i-1]])

        return memo[-1][-1]

    """
    TC: O(Size*N)
    SC: O(Size*N)
    """


sol2 = SolutionVariant2()
print(sol2.minNotes(N=12, arr=[2, 2, 5, 7, 1], index=4))
print(sol2.minNotesMemo(N=12, arr=[2, 2, 5, 7, 1], index=4, memo=[math.inf for _ in range(13)]))
print(sol2.minNotesBottomUp(N=12, arr=[2, 2, 5, 7, 1]))
