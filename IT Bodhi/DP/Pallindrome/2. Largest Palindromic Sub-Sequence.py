"""
Problem : Largest palindromic sub-sequence
Ex-: string = abkabNa  -> ababa

Approach 1: Using LCS
        Step 1: s1 = string
                s2 = reverse(string)
                and find LCS(s1, s2)

Approach 2: LPS Logic
    MLPS(i, j) =  MLPS(i+1, j-1) + 2  if arr[i] == arr[j]
                  max(MLPS(i+1, j), MLPS(i, j-1))

    TC: O(N^2)
    SC: O(N^2)
"""


class Solution:
    def maxLengthPalindromeSubSequence(self, s: str, start, end) -> int:
        # Base Case
        if start > end:
            return 0
        if start == end:
            return 1

        if s[start] == s[end]:
            return 2 + self.maxLengthPalindromeSubSequence(s, start+1, end-1)
        else:
            return max(self.maxLengthPalindromeSubSequence(s, start+1, end),
                       self.maxLengthPalindromeSubSequence(s, start, end-1))


sol = Solution()
print(sol.maxLengthPalindromeSubSequence(s="abkabNa", start=0, end=6))
