"""
In problems where we deal with sorted arrays (or LinkedLists) and need to find a set of elements that fulfill certain
constraints, the Two Pointers approach becomes quite useful. The set of elements could be a pair, a triplet or even a
sub-array.

Problem Statement : Given an array of unsorted numbers and a target number, find all unique quadruplets in it, whose sum
                    is equal to the target number.
Algo : This problem follows the Two Pointers pattern and shares similarities with Triplet Sum to Zero.
       We can follow a similar approach to iterate through the array, taking one number at a time. At every step during
       the iteration, we will search for the quadruplets similar to Triplet Sum to Zero whose sum is equal to the given
       target.


Example 1:
Input: [4, 1, 2, -1, 1, -3], target=1
Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
Explanation: Both the quadruplets add up to the target.

Example 2:
Input: [2, 0, -1, 1, -2, 2], target=2
Output: [-2, 0, 2, 2], [-1, 0, 1, 2]
Explanation: Both the quadruplets add up to the target.
"""
from typing import List
from collections import deque


class Quadruplets:
    @staticmethod
    def search_quadruplets(nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        quadruplets = []
        for i in range(0, len(nums) - 3):
            # Skip same element to avoid duplicate quadruplets
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums) - 2):
                # Skip same element to avoid duplicate quadruplets
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                Quadruplets.search_pairs(nums, target, i, j, quadruplets)
        return quadruplets

    @staticmethod
    def search_pairs(nums, target_sum, first, second, quadruplets):
        left = second+1
        right = len(nums) - 1
        while left < right:
            quad_sum = nums[first] + nums[second] + nums[left] + nums[right]
            if quad_sum == target_sum:  # Found the quadruplet
                quadruplets.append([nums[first], nums[second], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1  # Skip same element to avoid duplicate quadruplet
                while left < right and nums[right] == nums[right+1]:
                    right -= 1  # Skip same element to avoid duplicate quadruplet
            elif quad_sum < target_sum:
                left += 1  # We need a pair with a bigger sum
            else:
                right -= 1  # We need a pair with a smaller sum


def main():
    quad = Quadruplets()
    print(quad.search_quadruplets([4, 1, 2, -1, 1, -3], 1))
    print(quad.search_quadruplets([2, 0, -1, 1, -2, 2], 2))


main()


"""
Time Complexity: NLogN --> Sorting + N*N*N ==> O(N^3)
Space Complexity: O(N)
"""
