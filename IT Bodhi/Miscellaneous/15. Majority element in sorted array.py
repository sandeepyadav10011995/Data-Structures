"""
Problem : Majority element in sorted array.
Question: What does majority means?
If the element is present in array, and it's count > N/2; where N is the length/size of the array.
Pseudo Code -:
            - Step 1: Find the midValue
            - Step 2: Find the index of the midValue
            - Step 3: Check the number at index+N//2 is MidValue or not ?


TC: O(logN)
SC: O(1)
"""

class Solution:
    def findMajority(self, arr: list[int]) -> bool:
        N = len(arr)
        low = 0
        high = N-1
        mid = low + (high-low)//2
        midValue = arr[mid]
        # Get the first index of the midValue in the array using Binary Search
        firstIdx = self._binarySearch(arr, low, high, midValue)
        if firstIdx+N//2 < N-1 and arr[firstIdx+N//2] == midValue:
            return True
        else:
            return False
