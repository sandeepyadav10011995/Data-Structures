class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        rows = len(word1)
        cols = len(word2)

        # If either of them is empty
        if rows * cols == 0:
            return rows + cols

        # Create the DP Table
        dp_table = [[0 for col in range(cols + 1)] for row in range(rows + 1)]

        # Fill the first row of DP Table
        for col in range(1, cols + 1):
            dp_table[0][col] = col

        # Fill the first col of DP Table
        for row in range(1, rows + 1):
            dp_table[row][0] = row

        # Fill other cells
        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                if word1[row - 1] == word2[col - 1]:
                    dp_table[row][col] = dp_table[row - 1][col - 1]
                else:
                    dp_table[row][col] = min(dp_table[row - 1][col], dp_table[row - 1][col - 1],
                                             dp_table[row][col - 1]) + 1

        # Return the last cell
        return dp_table[-1][-1]

sol = Solution()
print(sol.minDistance('ephrem', 'benyam'))
