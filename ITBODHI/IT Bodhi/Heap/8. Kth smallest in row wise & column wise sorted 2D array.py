"""
Problem Statement: Kth smallest in row wise & column wise sorted 2D array.

Approach 1: Simple Min Heap Approach
            Make a MinHeap of all the elements --> O(N^2)
            Extract K elements --> 0(K*logN^2) ~ O(2K(logN))
            TC: O(N^2) + O(2K(logN))
            SC: O(N^2)

            Problem: When K <<<< N ?

Approach 2: Max Heap Approach
            Make a MaxHeap of K elements --> O(K)
            Now traverse the matrix and check if it can be inserted or not ?
            TC: O(N^2*logK) + O(K)
            SC: O(K)

Approach 3: Since the array is sorted row wise and column wise --> Therefore element will be found in K^2 matrix only
            Good Solution: When K <<<< N
            TC: O(K^2logK)
            SC: O(K)


Approach 4: Ugly Number Logic
            Insert the first element of the matrix in the minHeap
            Then;
                1. Pop the min element
                2. Add the right and down element if available in the minHeap
                3. Do this for K steps

            One Remove + 2 Addition ==> Max Length of Heap --> K

            TC: O(KlogK)
            SC: O(K)

"""
from heapq import *


class HeapNode:
    def __init__(self, val: int, row: int, col: int) -> None:
        self.val = val
        self.row = row
        self.col = col

    def __lt__(self, other):
        return self.val < other.val


class Matrix:
    @staticmethod
    def KthSmallestElement(matrix: list[list[int]], K: int) -> int:
        minHeap = []
        rows = len(matrix)
        cols = len(matrix[0])

        # Put the first element of the Matrix in the minHeap
        heappush(minHeap, HeapNode(val=matrix[0][0], row=0, col=0))

        kthSmallest = None
        uniqueNums = {matrix[0][0]}
        while K > 0:
            # Pop the min element
            node = heappop(minHeap)
            kthSmallest = node.val

            # Push the right and down element of the node if available
            if node.row + 1 < rows and matrix[node.row+1][node.col] not in uniqueNums:
                uniqueNums.add(matrix[node.row+1][node.col])
                heappush(minHeap, HeapNode(val=matrix[node.row+1][node.col], row=node.row+1, col=node.col))
            if node.col + 1 < cols and matrix[node.row][node.col+1] not in uniqueNums:
                uniqueNums.add(matrix[node.row][node.col+1])
                heappush(minHeap, HeapNode(val=matrix[node.row][node.col+1], row=node.row, col=node.col+1))

            K -= 1

        return kthSmallest


def main():
    matrix = Matrix()
    m = [[4, 8, 15, 21],
         [6, 11, 81, 159],
         [7, 16, 90, 205],
         [9, 17, 95, 307]
         ]
    for i in range(1, 17):
        print(f"{i}th Smallest number is : {matrix.KthSmallestElement(m, i)}")


main()
