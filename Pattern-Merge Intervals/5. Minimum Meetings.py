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


Question : Given a list of intervals representing the start and end time of ‘N’ meetings, find the minimum number of
           rooms required to hold all the meetings.
        Algo: Strategy
            1. We will sort the meetings based on start time
            2. We schedule a meeting m1 in room r1
            3. If the next meeting 
                If overlapping: meeting m2 --> room r2
                Else: meeting m2 --> room r1
            4. And so on
            
        So at any point of time we need to know which is that meeting going to get over next.
        ==> MinHeap based on "Meeting End time"

Example -:
Input : 
Output : 

------------------------------------CODE-----------------------------------
"""

from heapq import *


class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        # MinHeap Based on meetings End
        return self.end < other.end


class MinimumRooms:
    @staticmethod
    def minimumRoomsForMeetings(meetings: list) -> int:
        # Sort meetings based on start time
        meetings.sort(key=lambda x: x.start)  # TC: O(NlogN) SC: O(N)

        minRooms = 0
        minHeap = []

        for meeting in meetings:  # O(N) ==> TC: O(NlogN) SC: O(N)
            # Pop all the meetings from minHeap before this meeting
            while len(minHeap) > 0 and meeting.start >= minHeap[0].end:
                heappop(minHeap)  # O(logN)

            # push the meeting in minHeap
            heappush(minHeap, meeting)  # O(logN)

            # Update the minRooms --> At any moment of time what is the max num of meetings are going on !
            minRooms = max(minRooms, len(minHeap))

        return minRooms


def main():
    mr = MinimumRooms()
    print("Minimum meeting rooms required: " +
          str(mr.minimumRoomsForMeetings([Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))
    print("Minimum meeting rooms required: " +
          str(mr.minimumRoomsForMeetings([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)])))
    print("Minimum meeting rooms required: " +
          str(mr.minimumRoomsForMeetings([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)])))
    print("Minimum meeting rooms required: " +
          str(mr.minimumRoomsForMeetings([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)])))
    print("Minimum meeting rooms required: " +
          str(mr.minimumRoomsForMeetings([Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))


main()


"""
Overall TC : O(NlogN) + O(NlogN) --> O(NlogN)
Overall SC: O(N) + O(N) --> O(N)


Similar Problems#
Problem 1: Given a list of intervals, find the point where the maximum number of intervals overlap.

Problem 2: Given a list of intervals representing the arrival and departure times of trains to a train station, our 
           goal is to find the minimum number of platforms required for the train station so that no train has to wait.

Both of these problems can be solved using the approach discussed above.

"""
