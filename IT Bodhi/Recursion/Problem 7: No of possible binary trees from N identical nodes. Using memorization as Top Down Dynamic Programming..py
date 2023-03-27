"""

Here's a Python code that implements a top-down dynamic programming approach to find the number of possible binary
trees from N identical nodes:
"""


def BTFromNNodes(N: int) -> int:
    # Base Case
    if N == 0 or N == 1:
        return 1

    count = 0
    for i in range(N):
        count += BTFromNNodes(i) * BTFromNNodes(N-i-1)
    return count


"""
DP Solution
"""


def num_binary_trees(N):
    memo = [-1] * (N + 1)
    memo[0] = 1
    memo[1] = 1

    def helper(N):
        if memo[N] != -1:
            return memo[N]
        count = 0
        for i in range(N):
            count += helper(i) * helper(N - i - 1)
        memo[N] = count
        return count

    return helper(N)

