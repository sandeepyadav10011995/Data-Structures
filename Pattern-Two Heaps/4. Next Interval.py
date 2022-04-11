"""
In many problems, where we are given a set of elements such that we can divide them into two parts. We are interested
in knowing the smallest element in one part and the biggest element in the other part. The Two Heaps pattern is an
efficient approach to solve such problems.As the name suggests, this pattern uses two Heaps;
    Min Heap ---> smallest element
    Max Heap ---> biggest element

Problem Statement:  Given an array of intervals, find the next interval of each interval. In a list of intervals, for
                    an interval ‘i’ its next interval ‘j’ will have the smallest ‘start’ greater than or equal to the
                    ‘end’ of ‘i’.
            Write a function to return an array containing indices of the next interval of each input interval. If
            there is no next interval of a given interval, return -1. It is given that none of the intervals have the
            same start point.

Algo:   We can utilize the Two Heaps approach. We can push all intervals into two heaps: one heap to sort the intervals
        on maximum start time (let’s call it maxStartHeap) and the other on maximum end time (let’s call it maxEndHeap).
        We can then iterate through all intervals of the maxEndHeap to find their next interval. Our algorithm will have
        the following steps:
            1.  Take out the top (having highest end) interval from the maxEndHeap to find its next interval. Let’s call
                this interval topEnd.
            2.  Find an interval in the maxStartHeap with the closest start greater than or equal to the start of topEnd
                Since maxStartHeap is sorted by ‘start’ of intervals, it is easy to find the interval with the highest
                ‘start’. Let’s call this interval topStart.
            3.  Add the index of topStart in the result array as the next interval of topEnd. If we can’t find the next
                interval, add ‘-1’ in the result array.
            4.  Put the topStart back in the maxStartHeap, as it could be the next interval of other intervals.
            5.  Repeat steps 1-4 until we have no intervals left in maxEndHeap.


Example 1:
    Input: Intervals [[2,3], [3,4], [5,6]]
    Output: [1, 2, -1]
    Explanation: The next interval of [2,3] is [3,4] having index ‘1’. Similarly, the next interval of [3,4] is [5,6]
                 having index ‘2’. There is no next interval for [5,6] hence we have ‘-1’.

Example 2:
    Input: Intervals [[3,4], [1,5], [4,6]]
    Output: [2, -1, -1]
    Explanation: The next interval of [3,4] is [4,6] which has index ‘2’. There is no next interval for [1,5] and [4,6].

"""

from heapq import *


class Interval:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end


class NextInterval:
    @staticmethod
    def find_next_interval(intervals: list[Interval]) -> list[int]:
        n = len(intervals)

        # heaps for finding the maximum start and en
        max_start_heap, max_end_heap = [], []

        result = [0 for _ in range(n)]
        for end_index in range(n):
            heappush(max_start_heap, (-intervals[end_index].start, end_index))
            heappush(max_end_heap, (-intervals[end_index].end, end_index))

        # go through all the intervals to find each interval's next interval
        for _ in range(n):
            # let's find the next interval of the interval which has the highest 'end'
            top_end, end_index = heappop(max_end_heap)
            result[end_index] = -1  # default to -1
            if -max_start_heap[0][0] >= -top_end:
                top_start, start_index = heappop(max_start_heap)
                # find the the interval that has the closest 'start'
                while max_start_heap and -max_start_heap[0][0] >= -top_end:
                    top_start, start_index = heappop(max_start_heap)
                result[end_index] = start_index
                # put the interval back as it could be the next interval of other intervals
                heappush(max_start_heap, (top_start, start_index))

        return result


def main():
    ni = NextInterval()
    result = ni.find_next_interval([Interval(2, 3), Interval(3, 4), Interval(5, 6)])
    print("Next interval indices are: " + str(result))

    result = ni.find_next_interval([Interval(3, 4), Interval(1, 5), Interval(4, 6)])
    print("Next interval indices are: " + str(result))


main()
