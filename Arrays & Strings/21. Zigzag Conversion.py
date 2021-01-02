"""
Zigzag Conversion
Given a string s and an integer value rows return the "zigzag" encoding of s read off row-by-row.

Example 1:
Input:
s = "YELLOWPINK"
rows = 4

Output: "YPEWILONLK"
Explanation: There are 4 rows in the zigzag formatted string.

Y     P    (row 1: "YP")
E   W I    (row 2: "EWI")
L O   N    (row 3: "LON")
L     K    (row 4: "LK")

Example 2:
Input:
s = "REDBLUEBLACK"
rows = 2

Output: "RDLELCEBUBAK"
Explanation: There are 2 rows in the zigzag formatted string.

R D L E L C    (row 1: "RDLELC")
E B U B A K    (row 2: "EBUBAK")

Example 3:
Input:
s = "REDBLUEBLACK"
rows = 1

Output: "REDBLUEBLACK"
Explanation:

R E D B L U E B L A C K    (row 1: "REDBLUEBLACK")

Constraints:
rows > 0
"""

# Approach : Traverse the string in zig-zag manner.
#             IDEA : 1. Start at the first row and first character.
#                    2. Increase row and add character until the last row.
#                    3. Swap directions and go up and add characters, decrease the row.
#
#                   Time Complexity : O(max(n, rows))
#                   Space Complexity : O(max(n, rows))

class Solution:
    def zigzag(self, s, rows):
        output = [''] * rows
        down = False
        row = 0
        for c in s:
            output[row] += c
            if row == 0 or row == rows - 1:
                down = not down
            if rows > 1:
                row += 1 if down else -1

        return ''.join(output)
        # return self._combine(output)

    # def _combine(self, output):
    #     output_string = ""
    #     for row_string in output:
    #         output_string += row_string
    #     return output_string

s = 'YELLOWPINK'
rows = 4
sol = Solution()
print(sol.zigzag(s, rows))
