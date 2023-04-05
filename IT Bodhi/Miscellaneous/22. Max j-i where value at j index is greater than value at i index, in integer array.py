"""
Problem : Max j-i where value at j index is greater than value at i index, in integer array.
(i, j) --> Maximise(j-i+1) such that arr[j] > arr[i] and j > i --> Longest Sub-array

Example -: arr = [11, 4, 8, 6, 12, 9, 2, 7, 3]

Approach 1: Brute Force -: Check all the pairs
        TC: O(N^2)

Approach 2: Pair Sorting
        TC: O(NlogN)

Approach 3: Left Scan(minSoFar) + Right Scan(maxSoFar)
        arr: 11, 10, 8, 6, 12, 9, 2, 1, 3
        min: 11, 10, 8, 6,  6, 6, 2, 1, 1
        max: 12, 12, 12,12,12, 9, 3, 3, 3
        TC: O(N)
        SC: O(1)
Implement it !!
"""