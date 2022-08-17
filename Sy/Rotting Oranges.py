class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        - use BFS because no backtracking is needed
        - use counter to calculate levels
        
        2 1 1
        0 1 1
        1 0 1
        
        
        """
        row_size = len(grid)
        if row_size == 0:
            return 0
        col_size = len(grid[0])
        queue = []
        
        for row in range(row_size):
            for col in range(col_size):
                if grid[row][col] == 2:
                    queue.append([row, col, 0])
        
        def getNeighbors(i, j):
            neighbors = []
            if i > 0:
                neighbors.append([i-1, j])
            if i < row_size-1:
                neighbors.append([i+1, j])
            if j > 0:
                neighbors.append([i, j-1])
            if j < col_size-1:
                neighbors.append([i, j+1])            
            return neighbors
        
        minute_count = 0
        while len(queue) > 0:            
            node = queue.pop(0)
            minute_count = node[2]
            neighbors = getNeighbors(node[0], node[1])
            for i, j in neighbors:
                if grid[i][j] == 1:
                    grid[i][j] = 2
                    queue.append([i, j, minute_count+1])                    
        
        # check if rotten oranges still exist
        for row in range(row_size):
            for col in range(col_size):
                if grid[row][col] == 1:
                    return -1
                
        return minute_count
            
        
        
        
