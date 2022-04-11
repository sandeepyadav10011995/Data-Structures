"""
In many problems, where we are given a set of elements such that we can divide them into two parts. We are interested
in knowing the smallest element in one part and the biggest element in the other part. The Two Heaps pattern is an
efficient approach to solve such problems.As the name suggests, this pattern uses two Heaps;
    Min Heap ---> smallest element
    Max Heap ---> biggest element

Problem Statement:  Given an array of numbers and a number ‘k’, find the median of all the ‘k’ sized sub-arrays
                    (or windows) of the array.

Algo:   Similar to Find the Median of Number Stream.

        The only difference is that we need to keep track of a sliding window of ‘k’ numbers. This means, in each
        iteration, when we insert a new number in the heaps, we need to remove one number from the heaps which is going
        out of the sliding window. After the removal, we need to rebalance the heaps in the same way that we did while
        inserting.

Example 1:
    Input: nums=[1, 2, -1, 3, 5], k = 2
    Output: [1.5, 0.5, 1.0, 4.0]
    Explanation:    Lets consider all windows of size ‘2’:
                    [ 1, 2, -1, 3, 5] -> median is 1.5
                    [ 1, 2, -1, 3, 5] -> median is 0.5
                    [ 1, 2, -1, 3, 5] -> median is 1.0
                    [ 1, 2, -1, 3, 5] -> median is 4.0
Example 2:

    Input: nums=[1, 2, -1, 3, 5], k = 3
    Output: [1.0, 2.0, 3.0]
    Explanation:    Lets consider all windows of size ‘3’:
                    [ 1, 2, -1, 3, 5] -> median is 1.0
                    [ 1, 2, -1, 3, 5] -> median is 2.0
                    [ 1, 2, -1, 3, 5] -> median is 3.0

"""

import heapq
from heapq import *


class SlidingWindowMedian:
    def __init__(self) -> None:
        self.lower_half = []  # Containing first half of the numbers (MaxHeap)
        self.upper_half = []  # Containing second half of the numbers (MinHeap)

    def _rebalance_heaps(self) -> None:
        # either both the heaps will have equal number of elements or upper_half(min_heap) will have one
        # more element than the min-heap
        if len(self.upper_half) >= len(self.lower_half) + 2:
            heappush(self.lower_half, -heappop(self.upper_half))
        elif len(self.lower_half) >= len(self.upper_half) + 1:
            heappush(self.upper_half, -heappop(self.lower_half))

    def _remove(self, heap: list[int], element: int) -> None:
        # removes an element from the heap keeping the heap property
        idx = heap.index(element)  # find the element
        # move the element to the end and delete it
        heap[idx] = heap[-1]
        del heap[-1]
        # we can use heapify to re-adjust the elements but that would be O(N),
        # instead, we will adjust only one element which will be O(logN)
        if idx < len(heap):
            heapq._siftup(heap, idx)
            heapq._siftdown(heap, 0, idx)

    def findSlidingWindowMedian(self, nums: list[int], k: int) -> list[float]:
        window_start = 0
        result = [0.0 for _ in range(len(nums) - k + 1)]
        for window_end in range(0, len(nums)):
            if not self.upper_half or self.upper_half[0] <= nums[window_end]:
                heappush(self.upper_half, nums[window_end])
            else:
                heappush(self.lower_half, -nums[window_end])
            self._rebalance_heaps()

            # if we have at least 'k' elements in the sliding window
            if window_end >= k-1:
                # add the median to the the result array
                if len(self.lower_half) == len(self.upper_half):
                    result[window_start] = (-self.lower_half[0] + self.upper_half[0]) / 2
                else:
                    result[window_start] = (self.upper_half[0]) / 1

                # remove the element going out of the sliding window
                element_to_removed = nums[window_start]
                window_start += 1

                if element_to_removed >= self.upper_half[0]:
                    self._remove(self.upper_half, element_to_removed)
                else:
                    self._remove(self.lower_half, -element_to_removed)
                self._rebalance_heaps()

        return result


def main():
    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.findSlidingWindowMedian([1, 2, -1, 3, 5], 2)
    print("Sliding window medians are: " + str(result))

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.findSlidingWindowMedian([1, 2, -1, 3, 5], 3)
    print("Sliding window medians are: " + str(result))


main()


"""
Time Complexity: O(N*K) ==> Insert/Remove --> logK,  Searching the element to be removed --> O(K)
Space Complexity: O(K)
"""
