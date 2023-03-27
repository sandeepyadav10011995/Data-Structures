"""
Problem -: Days to rotten all tomatoes
Important Fact -:
    In this problem we have multiple sources.
    How we will get to know when all the tomatoes are rotten --> Queue is empty

-----------------------------  IMPORTANT NOTES ------------------------

TO FIND A CYCLE IN A GRAPH --> Do a DFS on that.
DP will not work whenever there is CYCLE in Recursive Relation. Therefore, use BFS.
2D Matrix Representation -: We have a unique representation of a cell to represent (i, j) as single attribute -:
                        CS -> Column Size, RS -> Row Size
                        (i, j) -->  (i*CS + j)
                        Example -: CS = 6, RS = 6, i = 3, j = 1
                        Final Value = 3*6+1 = 19
                        row = Final Value // CS = 19 // 6 = 3
                        col = FinalValue % CS = 19 % 6 = 1
"""
from collections import deque
from dataclasses import dataclass


@dataclass
class BFSNode:
    cellNo: int
    days: int


class Solution:
    @staticmethod
    def minDistBetweenSourceAndDestination(matrix, srcRow, srcCol):
        # 2--> Denotes Rotten
        # Else Not Rotten
        RS = len(matrix)
        CS = len(matrix[0])
        fresh = 0
        maxDays = 0
        directions = [0, 1, 0, -1, 0]
        visitedMap = {}  # Key: Value --> Cur Node: Prev/Parent Node
        bfsQueue = deque()
        for row in range(RS):
            for col in range(CS):
                if matrix[row][col] == 2:
                    bfsQueue.append(BFSNode(cellNo=srcRow*CS+srcCol, days=0))
                    visitedMap[srcRow*CS+srcCol] = 1
                else:
                    fresh += 1

        # Edge Case --> No Rotten Fruit in the matrix i.e, No source
        if not fresh:
            return 0

        # None i.e, end of the first level
        bfsQueue.append(None)

        while bfsQueue:
            bfsNode = bfsQueue.popleft()
            if bfsNode and bfsNode.cellNo > 0:
                row = bfsNode.cellNo // CS
                col = bfsNode.cellNo % CS

                # Explore all the Child Nodes (Neighbors)
                for k in range(4):
                    nRow = row + directions[k]
                    nCol = col + directions[k+1]
                    isInValidCoordinates = nRow < 0 or nRow == RS or nCol < 0 or nCol == CS
                    if isInValidCoordinates or \
                            matrix[nRow][nCol] == 2 or \
                            visitedMap.get(nRow * CS + nCol) is not None:
                        continue
                    else:
                        bfsQueue.append(BFSNode(cellNo=nRow * CS + nCol, days=bfsNode.days+1))
                        visitedMap[nRow * CS + nCol] = row * CS + col
                        maxDays = max(maxDays, bfsNode.days + 1)
                        fresh -= 1
            else:
                if bfsQueue:
                    bfsQueue.append(None)
        return -1 if fresh else maxDays


"""
TC: O(N*M)
SC: O(N*M)
"""



