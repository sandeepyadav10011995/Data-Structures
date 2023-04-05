"""
Problem : Find one non-repeated elements in an array

Approach 1: Using Hash Map
            TC: O(2N) ~ O(N)
            SC: O(N)

Approach 2: Using XOR Logic
            TC: O(N)
            SC: O(1)
"""

class Solution:
    @staticmethod
    def findElementAppearingOnceXORLogic(nums: list[int]) -> int:
        onceElement = 0
        for num in nums:
            onceElement ^= num

        return onceElement


sol = Solution()
print(sol.findElementAppearingOnceXORLogic(nums=[1, 1, 2, 3, 3, 4, 4]))
