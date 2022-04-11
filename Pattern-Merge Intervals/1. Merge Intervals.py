"""
    Merge Intervals -: This deals with overlapping intervals !
    In a lot of problems either we need to find overlapping intervals or merge intervals if they
    overlap.

    Case 1: A and B do not overlap.
    Case 2: A and B overlap, B ends after A.
    Case 3: A completely overlaps B.

    Case 4: A and B overlaps, A ends after B.
    Case 5: B completely overlaps A.
    Case 6: B and A do not overlaps.


Question. Given a list of intervals, merge all overlapping intervals to produce a list that has 
          mutually exclusive events.
          
          Lets take two intervals, say a and b
          Therefore a.start <= b.start
          ==>   Case 1: a.start, b.end
                Case 2: a.start, b.end
                Case 3: a.start, a.end
                Case 4: a.start, a.start
                
          On merging a, b --> c
          c.start = a.start
          c.end = max(a.start, b.end)
          
          Algo:
          1. If the len(intervals) < 2: return intervals
          2. Sort the intervals based on start time --> intervals.sort(lambda x: x.start)
          3. start = intervals[0].start
             end = intervals[0].end
          4. loop on intervals
             if interval.start < end: update the end ==> Overlap
             else:  Store the result ==> No overlap
                    Update the start and end
          
Example : Intervals = [[1, 4, [2, 5], [7, 9]]
Output : Merged Intervals = [[1, 5], [7, 9]]

"""
from __future__ import print_function

from typing import List


class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


class MergeIntervals:
    @staticmethod
    def mergeIntervals(intervals: List[Interval]) -> List[Interval]:
        # Base Case
        if len(intervals) < 2:
            return intervals

        # Sort the intervals based on start time
        intervals.sort(key=(lambda x: x.start))  # TC: O(NlogN) SC: O(N)

        start = intervals[0].start
        end = intervals[0].end
        merged_intervals = []

        for i in range(1, len(intervals)):  # TC: O(N) SC: O(N)
            interval = intervals[i]
            if interval.start <= end:  # Overlap
                # Update the end
                end = max(end, interval.end)
            else:
                merged_intervals.append(Interval(start, end))
                # Update the start and end
                start = interval.start
                end = interval.end
        # Add the last interval
        merged_intervals.append(Interval(start, end))
        return merged_intervals


def main():
    mi = MergeIntervals()

    print("Merged intervals: ", end='')
    for i in mi.mergeIntervals([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        i.print_interval()
        print()

    print("Merged intervals: ", end='')
    for i in mi.mergeIntervals([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
        i.print_interval()
        print()

    print("Merged intervals: ", end='')
    for i in mi.mergeIntervals([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
        i.print_interval()
        print()


main()


"""
Overall TC : O(NlogN) + O(N) --> O(NlogN)
Overall SC: O(N) + O(N) --> O(N)
"""
