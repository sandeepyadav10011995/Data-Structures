"""
F(i, j) = F(i-1, j) + F(i, j-1)

Here's a code in Python to find the total number of ways to move from the top-left to bottom-right of a 2D array by
taking only right or down steps, using a recursive approach:
"""


def number_of_ways(row, col):
    # Edge Case
    if row < 0 or col < 0:
        return 0
    # Base Case
    if row == 0 and col == 0:
        return 1

    return number_of_ways(row-1, col) + number_of_ways(row, col-1)


"""
Optimization : Memoization

"""


def number_of_ways(row, col, memo):
    # Edge Case
    if row < 0 or col < 0:
        return 0
    # Base Case
    if row == 0 and col == 0:
        return 1
    if memo[row][col] < 0:
        memo[row][col] = number_of_ways(row-1, col, memo) + number_of_ways(row, col-1, memo)

    return memo[row][col]

