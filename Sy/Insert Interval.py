"""
Explanation: If Any
"""

"""
Question : Insert a new interval in a list of intervals.
           Algo:
                1. Comes before the target and No overlaps
                2. Merge the overlaps
                3. Add other remaining intervals
Example -: -
Input : -
Output : -
"""

"""
------------------------------------CODE------------------------------------
"""


class InsertIntervals:
    @staticmethod
    def insertInterval(intervals: list, new_interval: list) -> list:
        merged_intervals = []
        i = 0
        N = len(intervals)
        start = 0
        end = 1

        # Come before a new_interval  --> No overlaps
        while i < N and intervals[i][end] < new_interval[start]:
            merged_intervals.append(intervals[i])
            i += 1
        # Merge the Overlaps
        while i < N and intervals[i][start] < new_interval[end]:
            new_interval[start] = min(intervals[i][start], new_interval[start])
            new_interval[end] = max(intervals[i][end], new_interval[end])
            i += 1
        # Insert the new_interval
        merged_intervals.append(new_interval)
        # Add the remaining intervals
        while i < N:
            merged_intervals.append(intervals[i])
            i += 1

        return merged_intervals


def main():
    II = InsertIntervals()
    print("Intervals after inserting the new interval: " + str(II.insertInterval([[1, 3], [5, 7], [8, 12]], [4, 6])))
    print("Intervals after inserting the new interval: " + str(II.insertInterval([[1, 3], [5, 7], [8, 12]], [4, 10])))
    print("Intervals after inserting the new interval: " + str(II.insertInterval([[2, 3], [5, 7]], [1, 4])))


main()

"""
Overall TC : O(N) --> O(N)
Overall SC: O(N) --> O(N)
"""
