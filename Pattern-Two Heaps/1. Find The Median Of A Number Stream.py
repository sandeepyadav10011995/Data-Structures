"""
In many problems, where we are given a set of elements such that we can divide them into two parts. We are interested
in knowing the smallest element in one part and the biggest element in the other part. The Two Heaps pattern is an
efficient approach to solve such problems.As the name suggests, this pattern uses two Heaps;
    Min Heap ---> smallest element
    Max Heap ---> biggest element

Problem Statement:  Design a class to calculate the median of a number stream. The class should have the following two
                    methods -:
    a.  insertNum(int num): stores the number in the class
    b.  findMedian(): returns the median of all numbers inserted in the class
    If the count of numbers inserted in the class is even, the median will be the average of the middle two numbers.

Algo:
    1.  smallestNumList --> MaxHeap
    2.  largeNumList --> MinHeap
    3.  Insertion --> LogN

Example 1:

1. insertNum(3)
2. insertNum(1)
3. findMedian() -> output: 2
4. insertNum(5)
5. findMedian() -> output: 3
6. insertNum(4)
7. findMedian() -> output: 3.5

"""

from heapq import *


class MedianOfAStream:
    def __init__(self) -> None:
        self.lower_half = []  # Containing first half of the numbers (MaxHeap)
        self.upper_half = []  # Containing second half of the numbers (MinHeap)

    def _rebalance(self) -> None:
        # either both the heaps will have equal number of elements or upper_half(min_heap) will have one
        # more element than the min-heap
        if len(self.upper_half) >= len(self.lower_half) + 2:
            heappush(self.lower_half, -heappop(self.upper_half))
        elif len(self.lower_half) >= len(self.upper_half) + 1:
            heappush(self.upper_half, -heappop(self.lower_half))

    def insertNum(self, num: int) -> None:
        if not self.upper_half or self.upper_half[0] <= num:
            heappush(self.upper_half, num)
        else:
            heappush(self.lower_half, -num)
        self._rebalance()

    def findMedian(self) -> float:
        if len(self.lower_half) == len(self.upper_half):
            return (-self.lower_half[0] + self.upper_half[0]) / 2
        return (self.upper_half[0]) / 1


def main():
    medianOfAStream = MedianOfAStream()
    medianOfAStream.insertNum(3)
    medianOfAStream.insertNum(1)
    print("The median is: " + str(medianOfAStream.findMedian()))
    medianOfAStream.insertNum(5)
    print("The median is: " + str(medianOfAStream.findMedian()))
    medianOfAStream.insertNum(4)
    print("The median is: " + str(medianOfAStream.findMedian()))


main()


"""
Time Complexity: O(logN)--> Insert and O(1) --> Find Median
Space Complexity: O(N)
"""