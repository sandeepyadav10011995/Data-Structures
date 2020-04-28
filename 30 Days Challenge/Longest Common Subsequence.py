"""
Given two strings text1 and text2, return the length of their longest common subsequence.
A subsequence of a string is a new string generated from the original string with some characters(can be none) 
deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). 
A common subsequence of two strings is a subsequence that is common to both strings.
If there is no common subsequence, return 0.

 

Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3 
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

"""
# Recursive Solution
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def lcs(s, t, m, n):
            if m == -1 or n == -1:
                return 0
            elif s[m] == t[n]:
                return 1 + lcs(s, t, m-1, n-1)
            else:
                return max(lcs(s, t, m-1, n), lcs(s, t, m, n-1))
        return lcs(text1, text2, len(text1)-1, len(text2)-1)
    
    
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
    
