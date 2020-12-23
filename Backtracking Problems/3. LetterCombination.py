class Solution:
    phone = {
        # '0': ['0'],
        # '1': ['1'],
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    output = []

    def _backtrack(self, combination, next_digits):
        if len(next_digits) == 0:
            self.output.append(combination)
        else:
            for letter in self.phone[next_digits[0]]:
                self._backtrack(combination + letter, next_digits[1:])

    def letterCombinations(self, digits):
        if digits:
            self._backtrack("", digits)
        return self.output

sol = Solution()
print(sol.letterCombinations('23'))
