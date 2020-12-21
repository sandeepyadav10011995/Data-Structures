"""
Given an array of integers arr, return true if and only if it is a valid mountain array.
Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Example 1:
Input: arr = [2,1]
Output: false

Example 2:
Input: arr = [3,5,5]
Output: false

Example 3:
Input: arr = [0,3,2,1]
Output: true

Constraints:
1 <= arr.length <= 104
0 <= arr[i] <= 104
"""


class Solution:
    def validMountainArray(self, nums):
        i, N = 0, len(arr)
        # Walk Up
        while i + 1 < N and nums[i] < nums[i + 1]:
            i += 1

        # Check Peak --> It can't be first and last
        if i == 0 or i == N - 1:
            return False

        # Walk Down
        while i + 1 < N and nums[i] > nums[i + 1]:
            i += 1

        return i == N - 1

arr = [0, 3, 2, 1]
sol = Solution()
print(sol.validMountainArray(arr))
