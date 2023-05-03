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
            # Remove the elements outside the current window : Remove head if it is arr[i]
            while window and window[0] <= index - k:
                window.popleft()

            # Remove the elements smaller than the current element from the right end of the window
            # Remove smaller elements from tail
            while window and nums[window[-1]] < nums[index]:
                window.pop()

            # Add the current element's --> index to the window
            window.append(index)

            # Add the maximum element of the current window to the result
            if index >= k - 1:
                maxVals.append(nums[window[0]])

        return maxVals


sol = Solution()
print(sol.maxWindowAllPositions(nums=[5, 4, 8, 3, 9, 10, 12, 5, 6, 9, 8, 13], k=3))


class Solution1:
    @staticmethod
    def minWindowAllPositions(nums: list[int], k: int):
        N = len(nums)
        if k > N:
            return []

        res = []
        window = deque()
        for idx in range(N):
            window.append(nums[idx])
            # Store the min value
            if idx >= k-1:
                res.append(min(window))
                window.popleft()
        return res

sol = Solution1()
print(sol.minWindowAllPositions(nums=[2,3,4,1,6,-9,10,23], k=3))
print(sol.minWindowAllPositions(nums=[2,3,4,6,6,-9,10,23], k=3))
"""
TC: O(N*K)
SC: O(K)
"""

class Solution2:
    @staticmethod
    def minWindowAllPositions(nums: list[int], k: int):
        N = len(nums)
        if k > N:
            return []

        res = []
        window = deque()

        for idx in range(N):
            while window and window[0] <= idx - k:
                window.popleft()

            while window and nums[window[-1]] > nums[idx]:
                window.pop()

            window.append(idx)

            if idx >= k - 1:
                res.append(nums[window[0]])

        return res


sol = Solution2()
print(sol.minWindowAllPositions(nums=[2,3,4,1,6,-9,10,23], k=3))
print(sol.minWindowAllPositions(nums=[2,3,4,6,6,-9,10,23], k=3))
"""
TC: O(N)
SC: O(K)
"""







