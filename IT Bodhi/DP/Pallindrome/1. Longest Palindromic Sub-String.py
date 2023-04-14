"""
Problem : Longest palindromic sub-string.

Ex -: string = "aptktplr"

F(i, j) = if arr[i] == arr[j] and isPalindrome(i+1, j-1) --> Return j-i+1
          else Return max(F(i+1, j), F(i, j-1))




"""


class Solution:
    @staticmethod
    def isPalindrome(arr, start, end):
        while start <= end:
            if arr[start] != arr[end]:
                return False
            start += 1
            end -= 1
        return True

    def maxLengthPalindrome(self, arr, start, end):
        # Base Case
        if start > end:
            return 0
        if start == end:
            return 1

        if arr[start] == arr[end] and self.isPalindrome(arr, start+1, end-1):
            return end-start+1
        else:
            return max(self.maxLengthPalindrome(arr, start+1, end), self.maxLengthPalindrome(arr, start, end-1))

    """
    TC: O(2^N)*N(Palindrome)
    SC: O(N) --> Call Stack
    """
    def maxLengthPalindromeMemo(self, arr, start, end, memo):
        # Base Case
        if start > end:
            return 0
        if start == end:
            return 1

        if memo[start][end] < 0:
            if arr[start] == arr[end] and self.isPalindrome(arr, start+1, end-1):
                memo[start][end] = end-start+1
            else:
                memo[start][end] = max(self.maxLengthPalindromeMemo(arr, start+1, end, memo),
                                       self.maxLengthPalindromeMemo(arr, start, end-1, memo))

        return memo[start][end]

        """
        TC: O(N^2)*N(Palindrome) ~ O(N^3)
        SC: O(N^2) --> Memo Matrix
        """


sol = Solution()
print(sol.maxLengthPalindrome(["a", "p", "t", "k", "t", "p", "l", "r"], 0, 7))
print(sol.maxLengthPalindromeMemo(["a", "p", "t", "k", "t", "p", "l", "r"], 0, 7,
                                  memo=[[-1 for _ in range(8)] for _ in range(8)]))


"""
F(i, j) ==> True if arr[i] == arr[j] and F(i+1, j-1) is True
            False Otherwise
            
For j-i+1 --> 1 + F(i+1, j-1)
Therefore we can get rid of the Palindrome Method !!
            
Important Logic --> There are two ways to fill DP Table
                    1. Fill Row By Row (Column By Column)
                    2. Fill For One Length, Two Length, Three Length, etc...

"""


def findMaxPalindrome(arr, dp):
    size = len(arr)
    # Fill the DP table w.r.t Length wise
    for strLength in range(2, size+1):  # Loop of Length of Sub-string
        for start in range(size-strLength+1):  # All sub-strings of length subLength
            # Base Case
            if strLength == 2:
                dp[start][start+1] = 2 if arr[start] == arr[start+1] else 1
            else:
                if arr[start] == arr[start+strLength-1] and dp[start+1][start+strLength-2] + 2 == strLength:
                    dp[start][start+strLength-1] = strLength
                else:
                    dp[start][start+strLength-1] = max(dp[start+1][start+strLength-1], dp[start][start+strLength-2])

    return dp[0][size-1]


"""
            ----------- Lengths ---------
            0   1   2   3   4   5   6   7   
            a   p   t   k   t   p   l   r
    0   a   1   1   1   1   3   5   5   5
    1   p       1   1   1   3   5   5   5   
    2   t           1   1   3   3   3   3  
    3   k               1   1   1   1   1
    4   t                   1   1   1   1   
    5   p                       1   1   1   
    6   l                           1   1
    7   r                               1
    
               
TC: O(N^2)
SC: O(N^2)
"""

