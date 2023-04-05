"""
Problem : Find two non-repeated elements in an array

Approach 1: Using Hash Map
            TC: O(2N) ~ O(N)
            SC: O(N)

Approach 2: Using XOR Logic :: Divide the arr in such a way that both subarray contains one non-repeated element each.
            How to do split array in that way ?
            Sol : Bits


            TC: O(N)
            SC: O(1)
"""

class Solution:
    @staticmethod
    def findElementsAppearingOnceXORLogic(nums: list[int]) -> int:
        onceElement = 0
        for num in nums:
            onceElement ^= num

        return onceElement


sol = Solution()
print(sol.findElementsAppearingOnceXORLogic(nums=[1, 1, 2, 3, 3, 4, 4]))
