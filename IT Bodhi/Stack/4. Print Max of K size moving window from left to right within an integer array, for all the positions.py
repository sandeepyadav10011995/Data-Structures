"""
Problem : Print Max of K size moving window from left to right within an integer array, for all the positions
Approach : Using Queue of K size --> Doubly Linked List Concept
This version uses a deque to store the indices of the elements in the current window, with the leftmost element at the
front of the deque and the rightmost element at the back. It also avoids recomputing the maximum of each window by
keeping track of the index of the maximum element in the window instead of the maximum value itself.

Amortized TC: O(N*K) ~ O(N)

"""
from collections import deque


class Solution:
    @staticmethod
    def maxWindowAllPositions(nums: list[int], k: int):
        size = len(nums)
        if k > size:
            return []

        maxVals = []
        window = deque()

        for index in range(size):
            # Remove the elements outside the current window
            while window and window[0] <= index - k:
                window.popleft()

            # Remove the elements smaller than the current element from the right end of the window
            while window and nums[window[-1]] < nums[index]:
                window.pop()

            # Add the current element's --> index to the window
            window.append(index)

            # Add the maximum element of the current window to the result
            if index >= k - 1:
                maxVals.append(nums[window[0]])

        return maxVals
