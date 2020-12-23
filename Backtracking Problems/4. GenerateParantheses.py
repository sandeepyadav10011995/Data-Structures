class Solution:
    def __init__(self):
        self.output = []

    def _helper(self, op, cl, string, n):
        if len(string) == 2 * n:
            self.output.append(string)
            return
        if op > 0:
            self._helper(op - 1, cl, string + "(", n)
        if op < cl:
            self._helper(op, cl - 1, string + ")", n)

    def generateParenthesis(self, n):
        self._helper(n, n, "", n)
        return self.output

sol = Solution()
print(sol.generateParenthesis(n=5))
