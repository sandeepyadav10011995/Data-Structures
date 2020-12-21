"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

class Solution:
    def moveZeroes(self, nums):
        """
            Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        left = 0
        right = 0
        while right < N:
            if nums[left] == 0 and nums[right] != 0:
                # Swap
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            elif nums[right] == 0:
                right += 1
            else:
                left += 1
                right += 1
        return nums

arr = [0,1,0,3,12]
sol = Solution()
print(sol.moveZeroes(arr))
