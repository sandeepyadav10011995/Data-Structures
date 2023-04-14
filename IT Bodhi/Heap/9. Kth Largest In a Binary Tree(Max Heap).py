"""
Problem Statement: Kth Largest in A Binary Tree (Max Heap)

Approach 1: If K is in the order of N, then Quick Sort partition --> O(N)

Approach 2: Next Largest --> Ugly Number Logic
            Use a MaxHeap
            Insert the first element of the array in the maxHeap
            Then;
                1. Pop the max element
                2. Add the right and down element if available in the minHeap
                3. Do this for K steps
            TC: O(K*logK)
            SC: O(K)

"""
from heapq import *


class BinaryTree:
    @staticmethod
    def kthLargestNumber(nums: list[int], K: int) -> int:
        maxHeap = []

        # Insert the first element in the maxHeap
        heappush(maxHeap, (-nums[0], 0))

        kthLargestNumber = None
        while K > 0:
            # Pop the max element
            val, idx = heappop(maxHeap)
            kthLargestNumber = -val

            # Push the left and right child if present in the maxHeap
            if 2*idx+1 < len(nums):
                heappush(maxHeap, (-nums[2*idx+1], 2*idx+1))
            if 2*idx+2 < len(nums):
                heappush(maxHeap, (-nums[2*idx+2], 2*idx+2))

            K -= 1

        return kthLargestNumber


def main():
    bt = BinaryTree()
    array = [50, 40, 35, 20, 15, 32, 31, 8, 3, 10, 6]
    for i in range(1, 12):
        print(f"{i}th Largest number is : {bt.kthLargestNumber(array, i)}")


main()





