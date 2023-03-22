"""
F(i, j) = max(F(i, j-1), F(i-1, j), F(i-1, j-1)) + grid[i][j]


Case 1: Whenever we are trying to MAXIMIZE, for the edge cases we return a big MIN value.
"""

import math


def getMaxCoins(i, j, grid):
    # Edge Case
    if i < 0 or j < 0:
        return -math.inf

    return grid[i][j] + \
        max(getMaxCoins(i - 1, j, grid),
            getMaxCoins(i, j - 1, grid),
            getMaxCoins(i - 1, j - 1, grid))


"""
Case 2: What if there are some hurdles ==> Then treat the hurdles values as MIN values
"""

"""
Case 3: Follow Up -: You cannot reach a point i.e. you cannot take certain distance, i.e., they are unreachable.
*-----1--->Right
| \
2   3 
|     \
Down    Diagonal


F(i, j) = max( F(i, j-1) - 1,
               F(i-1, j) - 2,
               F(i-1, j-1) - 3
             ) + grid[i][j]

"""


def getMaxCoins2(i, j, grid):
    # Edge Case
    if i < 0 or j < 0:
        return -math.inf

    right = -math.inf if getMaxCoins2(i - 1, j, grid) < 0 else getMaxCoins2(i - 1, j, grid)
    down = -math.inf if getMaxCoins2(i, j - 1, grid) < 0 else getMaxCoins2(i, j - 1, grid)
    diagonal = -math.inf if getMaxCoins2(i - 1, j - 1, grid) < 0 else getMaxCoins2(i - 1, j - 1, grid)

    return grid[i][j] + max(right, down, diagonal)


"""
DP Solution
"""


def max_coins(grid):
    memo = [[0] * len(grid[0]) for _ in range(len(grid))]
    memo[0][0] = grid[0][0]

    for i in range(1, len(grid)):
        memo[i][0] = memo[i - 1][0] + grid[i][0]

    for j in range(1, len(grid[0])):
        memo[0][j] = memo[0][j - 1] + grid[0][j]

    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            memo[i][j] = max(memo[i - 1][j - 1], memo[i - 1][j], memo[i][j - 1]) + grid[i][j]

    return memo[-1][-1]
