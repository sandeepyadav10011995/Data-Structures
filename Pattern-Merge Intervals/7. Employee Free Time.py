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

Question : For ‘K’ employees, we are given a list of intervals representing each employee’s working hours.
           Our goal is to determine if there is a free interval which is common to all employees.
           You can assume that each list of employee working hours is sorted on the start time.
Example -:
Input :
Output :

------------------------------------CODE-----------------------------------
"""
from __future__ import print_function
from heapq import *


class Interval:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


class EmployeeInterval:
    def __init__(self, interval: Interval, empIdx: int, intIdx: int) -> None:
        self.interval = interval
        self.empIdx = empIdx
        self.intIdx = intIdx

    def __lt__(self, other):
        # MinHeap based on Intervals start time
        return self.interval.start < other.interval.start


class EmployeeFreeTime:
    @staticmethod
    def find_employee_free_time(schedule: list[list[Interval]]) -> list[Interval]:
        # Base Case
        if schedule is None:
            return []
        N = len(schedule)
        result = []
        minHeap = []

        # Put all the employee's first interval in minHeap
        for i in range(N):
            heappush(minHeap, EmployeeInterval(interval=schedule[i][0], empIdx=i, intIdx=0))

        prev_interval = minHeap[0].interval
        while minHeap:
            queue_top = heappop(minHeap)
            # If the previous interval is not overlapping with current interval --> Free Interval
            if prev_interval.end < queue_top.interval.start:
                result.append(Interval(start=prev_interval.end, end=queue_top.interval.start))
                # Update the Previous Interval
                prev_interval = queue_top.interval
            else:
                # Update the Previous Interval if needed
                if prev_interval.end < queue_top.interval.end:
                    prev_interval = queue_top.interval

                # If there are more items available for the employee's --> add it to minHeap
                emp_schedule = schedule[queue_top.empIdx]
                if len(emp_schedule) > queue_top.intIdx + 1:
                    heappush(
                        minHeap, EmployeeInterval(
                            interval=emp_schedule[queue_top.intIdx+1],
                            empIdx=queue_top.empIdx,
                            intIdx=queue_top.intIdx+1
                        )
                    )

        return result


def main():
    eft = EmployeeFreeTime

    input1 = [[Interval(1, 3), Interval(5, 6)], [Interval(2, 3), Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in eft.find_employee_free_time(input1):
        interval.print_interval()
    print()

    input2 = [[Interval(1, 3), Interval(9, 12)], [Interval(2, 4)], [Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in eft.find_employee_free_time(input2):
        interval.print_interval()
    print()

    input3 = [[Interval(1, 3)], [Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]
    print("Free intervals: ", end='')
    for interval in eft.find_employee_free_time(input3):
        interval.print_interval()
    print()


main()


"""
Overall TC : O(NlogK) --> O(NloK)
Overall SC: O(K) --> O(K)
"""
