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

Question : We are given a list of Jobs. Each job has a Start time, an End time, and a CPU load when it is running.
           Our goal is to find the maximum CPU load at any time if all the jobs are running on the same machine.
        Algo:
            The problem follows the Merge Intervals pattern and can easily be converted to Minimum Meeting Rooms.
            Similar to ‘Minimum Meeting Rooms’ where we were trying to find the maximum number of meetings happening at
            any time, for ‘Maximum CPU Load’ we need to find the maximum number of jobs running at any time.
            We will need to keep a running count of the maximum CPU load at any time to find the overall maximum load.

Example -:
Input : 
Output :
------------------------------------CODE-----------------------------------
"""

from heapq import *


class Job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load

    def __lt__(self, other):
        # MinHeap based on jobs end time
        return self.end < other.end


class CPULoad:
    @staticmethod
    def max_cpu_load(jobs: list[Job]) -> int:
        # Sort the jobs based on start time
        jobs.sort(key=lambda x: x.start)  # TC: O(NlogN) SC: O(N)

        max_cpu_load = 0
        cur_cpu_load = 0
        minHeap = []

        for job in jobs:  # O(N) ==> TC: O(NlogN) SC: O(N)
            # Pop all the jobs from minHeap before this job
            while len(minHeap) > 0 and job.start >= minHeap[0].end:
                cur_cpu_load -= minHeap[0].cpu_load
                heappop(minHeap)  # O(logN)
            # push the job in minHeap
            heappush(minHeap, job)  # O(logN)
            cur_cpu_load += job.cpu_load
            # Update the max_cpu_load --> At any moment of time what is the max num of jobs are going on !
            max_cpu_load = max(max_cpu_load, cur_cpu_load)

        return max_cpu_load


def main():
    cpl = CPULoad()
    print("Maximum CPU load at any time: " + str(cpl.max_cpu_load([Job(1, 4, 3), Job(2, 5, 4), Job(7, 9, 6)])))
    print("Maximum CPU load at any time: " + str(cpl.max_cpu_load([Job(6, 7, 10), Job(2, 4, 11), Job(8, 12, 15)])))
    print("Maximum CPU load at any time: " + str(cpl.max_cpu_load([Job(1, 4, 2), Job(2, 4, 1), Job(3, 6, 5)])))


main()


"""
Overall TC : O(NlogN) + O(NlogN) --> O(NlogN)
Overall SC: O(N) + O(N) --> O(N)
"""
