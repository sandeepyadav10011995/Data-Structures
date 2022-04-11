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

"""

"""
Question : Given an array of intervals representing ‘N’ appointments, find out if a person can attend 
           all the appointments.
    Algo:
        1. Sort the intervals/appointments based on start time.
        2. loop over appointments
            if any overlap: --> return False
            else: --> continue
        3. return True
        
Example -:
Input : 
Output : 

"""


"""
------------------------------------CODE-----------------------------------
"""


class ConflictingAppointments:
    @staticmethod
    def canAttendAll(intervals: list) -> bool:
        # Sort the appointments w.r.t start time
        intervals.sort(key=lambda x: x[0])  # O(NlogN)

        start, end = 0, 1
        for i in range(1, len(intervals)):  # O(N)
            if intervals[i][start] < intervals[i-1][end]:
                return False

        return True


def main():
    ca = ConflictingAppointments()
    print("Can attend all appointments: " + str(ca.canAttendAll([[1, 4], [2, 5], [7, 9]])))
    print("Can attend all appointments: " + str(ca.canAttendAll([[6, 7], [2, 4], [8, 12]])))
    print("Can attend all appointments: " + str(ca.canAttendAll([[4, 5], [2, 3], [3, 6]])))


main()


"""
Overall TC : O(NlogN) + O(N) --> O(NlogN)
Overall SC: O(N) + O(1) --> O(N)
"""