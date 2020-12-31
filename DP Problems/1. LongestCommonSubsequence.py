def longestCommonSubsequence(text1: str, text2: str) -> int:
    # Recursion --> Time Limit Exceeded
    # def lcs(s, t, i, j):
    #     if i == -1 or j == -1:
    #         return 0
    #     elif s[i] == t[j]:
    #         return 1 + lcs(s, t, i-1, j-1)
    #     else:
    #         return max(lcs(s, t, i-1, j), lcs(s, t, i, j-1))
    # return lcs(text1, text2, len(text1)-1, len(text2)-1)

    # DP Solution
    m = len(text1)
    n = len(text2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]
    print(dp, m, n)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    print(dp)
    return dp[-1][-1]

# print(longestCommonSubsequence("abcde", "ace"))
print(longestCommonSubsequence("GXTXAYB", "AGGTAB"))
