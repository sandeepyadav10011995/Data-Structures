"""
You can call the function find_largest_water_body by passing in a 2D matrix of 0s and 1s as an argument. The function
will return the size of the largest water body in the matrix.

Here's a Python solution that uses a recursive approach to find the largest water body in a 2D matrix of 0s and 1s:
"""


def _wbs(i, j, rs, cs, grid):
    if i < 0 or i >= rs or j < 0 or j >= cs or grid[i][j] != 0:
        return 0
    # Mark the call as visited
    grid[i][j] = -1

    return 1 + \
        _wbs(i - 1, j, rs, cs, grid) + \
        _wbs(i + 1, j, rs, cs, grid) + \
        _wbs(i, j - 1, rs, cs, grid) + \
        _wbs(i, j + 1, rs, cs, grid)


def find_largest_water_body(grid):
    max_size = 0
    rs = len(grid)
    cs = len(grid[0])
    for i in range(rs):
        for j in range(cs):
            if grid[i][j] == 0:
                max_size = max(max_size, _wbs(i, j, rs, cs, grid))
    return max_size


"""
Dp Solution
"""


# def find_largest_water_body_2(matrix):
#     max_size = 0
#     rows = len(matrix)
#     cols = len(matrix[0])
#     visited = [[False for j in range(cols)] for i in range(rows)]
#
#     def dfs(i, j):
#         if 0 <= i < rows and 0 <= j < cols and not visited[i][j] and matrix[i][j] == 0:
#             visited[i][j] = True
#             size = 1
#             size += dfs(i + 1, j)
#             size += dfs(i - 1, j)
#             size += dfs(i, j + 1)
#             size += dfs(i, j - 1)
#             return size
#         return 0
#
#     for i in range(rows):
#         for j in range(cols):
#             if matrix[i][j] == 0 and not visited[i][j]:
#                 size = dfs(i, j)
#                 max_size = max(max_size, size)
#     return max_size
