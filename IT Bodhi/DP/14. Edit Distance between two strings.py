"""
-------------- Leveistein Distance -------------
Problem : Edit Distance between two strings.
F(i, j) = F(i-1, j-1) if w1[i] == w2[j]
        = 1 + min(F(i-1, j-1), F(i-1, j), F(i, j-1))  Otherwise
Approach 1: Recursive
        TC: O(3^(M+N))
        SC: O(M+N) --> Call Stack
Approach 2: Top-Down
        TC: O(3*M*N)
        SC: O(M*N)
Approach : Bottom Up
        TC: O(M*N)
        SC: O(M*N)
Follow Up -: Can you optimize the space?

"""


class Solution:
    def editDistance(self, word1, word2, i, j):
        # Base Case
        if i < 0:  # word1 is ""
            return j+1
        if j < 0:  # word2 is ""
            return i+1
        if word1[i-1] == word2[j-1]:
            return self.editDistance(word1, word2, i-1, j-1)

        return 1 + \
            min(self.editDistance(word1, word2, i-1, j-1),  # Update
                self.editDistance(word1, word2, i, j-1),  # Insert
                self.editDistance(word1, word2, i-1, j)  # Delete
                )

    def editDistanceMemo(self, word1, word2, i, j, memo):
        # Base Case
        if i < 0:  # word1 is ""
            return j+1
        if j < 0:  # word2 is ""
            return i+1
        if memo[i][j] < 0:
            if word1[i-1] == word2[j-1]:
                memo[i][j] = self.editDistance(word1, word2, i-1, j-1)
            else:
                memo[i][j] = 1 + \
                    min(self.editDistanceMemo(word1, word2, i-1, j-1, memo),  # Update
                        self.editDistanceMemo(word1, word2, i, j-1, memo),  # Insert
                        self.editDistanceMemo(word1, word2, i-1, j, memo)  # Delete
                        )
        return memo[i][j]

    @staticmethod
    def editDistanceBottomUp(word1, word2):
        rows = len(word1)
        cols = len(word2)
        # Base Case
        if rows*cols == 0:  # If either of them is empty
            return rows+cols
        memo = [[0 for _ in range(cols+1)] for _ in range(rows+1)]
        # Fill the first row of memo table
        for col in range(cols+1):
            memo[0][col] = col
        # Fill the first row of memo table
        for row in range(rows+1):
            memo[row][0] = row

        for row in range(1, rows+1):
            for col in range(1, cols+1):
                if word1[row-1] == word2[col-1]:
                    memo[row][col] = memo[row-1][col-1]
                else:
                    memo[row][col] = 1 + \
                                     min(
                                         memo[row-1][col-1],  # Update
                                         memo[row-1][col],  # Insert
                                         memo[row][col-1]  # Delete
                                     )

        return memo[-1][-1]  # Return the last cell

    @staticmethod
    def editDistanceBottomUpOptimized(word1, word2):
        rows = len(word1)
        cols = len(word2)
        # Base Case
        if rows * cols == 0:  # If either of them is empty
            return rows + cols
        even_memo = [i for i in range(rows+1)]
        odd_memo = [0 for _ in range(rows+1)]
        odd_memo[0] = 1
        for t in range(1, cols+1):
            if t % 2 == 1:
                cur_memo = odd_memo
                prev_memo = even_memo
            else:
                cur_memo = even_memo
                prev_memo = odd_memo
            cur_memo[0] = t
            for d in range(1, rows+1):
                if word2[t-1] == word1[d-1]:
                    cur_memo[d] = prev_memo[d-1]
                else:
                    cur_memo[d] = min(prev_memo[d-1], prev_memo[d], cur_memo[d-1]) + 1
        return even_memo[-1] if cols % 2 == 0 else odd_memo[-1]  # Return the last cell


sol = Solution()
print(sol.editDistance(word1="ephrem", word2="benyam", i=5, j=5))
memo = [[-1 for _ in range(6)] for _ in range(6)]
for i in range(6):
    memo[i][0] = i
for i in range(6):
    memo[0][i] = i
print(sol.editDistanceMemo(word1="ephrem", word2="benyam", i=5, j=5, memo=memo))
print(sol.editDistanceBottomUp(word1="ephrem", word2="benyam"))
print(sol.editDistanceBottomUpOptimized(word1="ephrem", word2="benyam"))
