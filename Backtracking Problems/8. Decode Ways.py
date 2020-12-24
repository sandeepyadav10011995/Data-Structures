class Solution:
    def _recur(self, s, decode_pointer, dp):
        if decode_pointer >= len(s):
            return 1
        if dp[decode_pointer] > -1:
            return dp[decode_pointer]

        answer = 0
        for i in range(1, 3):
            if decode_pointer + i <= len(s):
                subst = s[decode_pointer:decode_pointer + i]
                if 1 <= int(subst) <= 26 and not subst.find('0') == 0:
                    answer += self._recur(s, decode_pointer + i, dp)
        dp[decode_pointer] = answer
        return dp[decode_pointer]

    def numDecodings(self, s: str) -> int:
        dp = [-1] * len(s)
        return self._recur(s, 0, dp)

sol = Solution()
print(sol.numDecodings('2263'))
