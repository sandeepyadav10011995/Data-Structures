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
Question : Given two lists of intervals, find the intersection of these two lists. 
           Each list consists of disjoint intervals sorted on their start time.
        Algo: Lets take two interval a and b --> Overlap then
        Case 1: A overlaps B
        A       s----------------e
        B   s---------e
        Case 2: B overlaps A
        A   s---------e
        B       s----------------e
        
        if either case then C
            1. C.start = max(A.start, B.start)
            2. C.end = min(A.end, B.end)
            
Example -:
Input : 
Output : 

"""


"""
------------------------------------CODE-----------------------------------
"""


class IntervalIntersections:
    @staticmethod
    def intervalIntersections(intervalA: list, intervalB: list) -> list:
        result = []
        i, j = 0, 0
        start, end = 0, 1

        while i < len(intervalA) and j < len(intervalB):
            a_overlaps_b = intervalB[j][start] <= intervalA[i][start] < intervalB[j][end]
            b_overlaps_a = intervalA[i][start] <= intervalB[j][start] < intervalA[i][end]

            if a_overlaps_b or b_overlaps_a:
                result.append([max(intervalA[i][start], intervalB[j][start]), min(intervalA[i][end], intervalB[j][end])])

            if intervalA[i][end] < intervalB[j][end]:
                i += 1
            else:
                j += 1
        return result


def main():
    II = IntervalIntersections()
    print("Intervals Intersection: " + str(II.intervalIntersections([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
    print("Intervals Intersection: " + str(II.intervalIntersections([[1, 3], [5, 7], [9, 12]], [[5, 10]])))


main()

"""
Overall TC :  O(N + M) --> O(N + M)
Overall SC: O(1) --> Ignoring the output space.
"""