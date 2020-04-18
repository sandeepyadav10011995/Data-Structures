"""
Leet Code --> Walls and Gates Problem

Example :
Input = 
[[INF, -1, 0, INF]
 [INF, INF, INF, -1]
 [INF, -1, INF, -1]
 [0, -1, INF, INF]]

Output = 
[[3, -1, 0, 1]
 [2, 2, 1, -1]
 [1, -1, 2, -1]
 [0, -1, 3, 4]]

"""

class Solution:
    def getNeighbors(self, row: int, col: int, rows: int, cols: int) -> List[(int)]:
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
    
    def wallsAndGates(self, rooms: List[List[int]]) -> List[List[int]]:
        rows = len(rooms)
        # Edge Case
        if rows == 0:
            return []
        cols = len(rooms[0])
        
        # Loop through the room to find the gates
        queue = []
        for row in range(rows):
            for col in range(cols):
                # Check if it is a gate
                if rooms[row][col] == 0:
                    queue.append((row, col))
        # Start BFS
        while queue:
            r, c = queue.pop(0)
            for nr, nc in self.getNeighbors(r, c, rows, cols):
                if rooms[nr][nc] != INF:
                    continue
                grid[nr][nc] = min(grid[r][c] + 1, grid[nr][nc])
                queue.append((nr, nc))
        return rooms




