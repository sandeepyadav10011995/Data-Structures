"""
Given a rotated sorted array, find the minimum element.

A "rotated" array is an array that has had each item shifted to the left or right by k units (where k is a positive integer) while maintaining positional integrity of every element in the original array.

Example 1:
Input: [4, 5, 6, 7, 1, 2]
Output: 1

Example 2:
Input: []
Output: -1

Example 3:
Input: [55, 88, 91, 93, 2, 9, 20]
Output: 2

Follow-Up:
Can you do this in O(log(n)) time?

Constraints:
arr[i] >= 0
"""

class Solution:
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + ((right-left) // 2)
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left] if len(nums) > 0 else -1

sol = Solution()
print(sol.findMin([55, 88, 91, 93, 2, 9, 20]))
  
