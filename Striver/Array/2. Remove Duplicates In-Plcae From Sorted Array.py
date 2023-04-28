"""
Problem -: Remove Duplicates In-Place From Sorted Array

Brute Force Approach -: Using Set
             TC: O(N*logN) --> In C++, O(N) --> Python
             SC: O(N)

Optimal Approach -: Using Two Pointers Approach

"""


class Solution:
    @staticmethod
    def removeDuplicatesFromArray(nums: list[int]) -> int:
        N = len(nums)
        if N == 0:
            return -1

        left = 0
        for right in range(1, N):
            if nums[right] != nums[left]:
                nums[left+1] = nums[right]
                left += 1

        return left + 1


sol = Solution()
print(sol.removeDuplicatesFromArray(nums=[1, 1, 2, 2, 3, 3, 4, 4, 5]))
