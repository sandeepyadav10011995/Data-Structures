"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input:
11110
11010
11000
00000
Output: 1

Example 2:
Input:
11000
11000
00100
00011
Output: 3
"""

class Solution:
    def getNeighbors(self, row: int, col: int, rows: int, cols: int) -> List[(int, int)]:
        neighbors = []
        if row > 0:
            neighbors.append((row-1, col))
        if row < rows-1:
            neighbors.append((row+1, col))
        if col > 0:
            neighbors.append((row, col-1))
        if col < cols-1:
            neighbors.append((row, col+1))
        return neighbors
        
    def checkIslands(self, row: int, col: int, grid: List[List[str]], rows: int, cols: int) -> None:
        queue = [(row, col)]
        grid[row][col] = 0
        while queue:
            r, c = queue.pop(0)
            for nr, nc in self.getNeighbors(r, c, rows, cols):
                if grid[nr][nc] == "1":
                    grid[nr][nc] = 0
                    queue.append((nr, nc))
        
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        # Edge Case 
        if rows == 0:
            return 0
        cols = len(grid[0])
        count = 0
        # Loop through the grid to find islands
        for row in range(rows):
            for col in range(cols):
                # Check if it is island
                if grid[row][col] == "1":
                    # Start BFS
                    print("start")
                    self.checkIslands(row, col, grid, rows, cols)
                    count += 1
                    print(count)
        return count



