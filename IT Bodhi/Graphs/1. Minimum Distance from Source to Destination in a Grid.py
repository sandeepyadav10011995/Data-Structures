"""
Problem -: Minimum distance from source to destination in a Grid

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
class LevelNode:
    row: int
    col: int
    level: int


class Solution:
    @staticmethod
    def minDistBetweenSourceAndDestination(matrix, srcRow, srcCol, destRow, destCol):
        INF = 2**31 - 1
        RS = len(matrix)
        CS = len(matrix[0])
        dist = 0
        directions = [0, 1, 0, -1, 0]
        visitedMap = {}
        bfsQueue = deque()
        bfsQueue.append(srcRow*CS + srcCol)
        visitedMap[srcRow*CS + srcCol] = 1
        # -1 Denotes None i.e, end of the level
        bfsQueue.append(-1)

        while bfsQueue:
            element = bfsQueue.popleft()
            if element > 0:
                row = element // CS
                col = element % CS

                # Found The Destination
                if row == destRow and col == destCol:
                    return dist

                # Explore all the Child Nodes (Neighbors)
                for k in range(4):
                    nRow = row + directions[k]
                    nCol = col + directions[k+1]
                    isInValidCoordinates = nRow < 0 or nRow == RS or nCol < 0 or nCol == CS
                    if isInValidCoordinates or \
                            matrix[nRow][nCol] == INF or \
                            visitedMap.get(nRow * CS + nCol) is not None:
                        continue
                    else:
                        bfsQueue.append(nRow * CS + nCol)
                        visitedMap[nRow * CS + nCol] = 1
            else:
                if bfsQueue:
                    bfsQueue.append(-1)
                    dist += 1
        return -1


"""
TC: O(N*M)
SC: O(N*M)
"""
