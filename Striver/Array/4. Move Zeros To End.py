"""
Problem: Move Zeros To End

BruteForce Solution -: Store the non-zero elements in another array
                       Copy the non-zero array to nums and replace all the remaining index with 0

Optimal Solution -: Two Pointers With Swapping
                    Step 1: Find the Start of the Zero In the Array (Using Break)
                    Step 2: Iterate over the array and when we encounter
"""


class Solution:
    @staticmethod
    def moveZerosToEnd(nums: list[int], N: int) -> list[int]:
        right = -1
        for i in range(N):
            if nums[i] == 0:
                right = i
                break

        # Non-Zero numbers
        if right == -1:
            return nums

        for left in range(right+1, N):
            if nums[left] != 0:
                # Swap
                nums[left], nums[right] = nums[right], nums[left]
                right += 1
        return nums


sol = Solution()
print(sol.moveZerosToEnd(nums=[1, 0, 2, 3, 2, 0, 0, 4, 5, 1], N=10))
