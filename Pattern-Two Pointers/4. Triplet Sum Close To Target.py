"""
In problems where we deal with sorted arrays (or LinkedLists) and need to find a set of elements that fulfill certain
constraints, the Two Pointers approach becomes quite useful. The set of elements could be a pair, a triplet or even a
sub-array.

Problem Statement : Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as
                    close to the target number as possible, return the sum of the triplet. If there are more than one
                    such triplet, return the sum of the triplet with the smallest sum.

Algo : This problem follows the Two Pointers pattern and is quite similar to Triplet Sum to Zero.
       We can follow a similar approach to iterate through the array, taking one number at a time. At every step, we
       will save the difference between the triplet and the target number, so that in the end, we can return the triplet
       with the closest sum.

Example 1:
Input: [-2, 0, 1, 2], target=2
Output: 1
Explanation: The triplet [-2, 1, 2] has the closest sum to the target.

Example 2:
Input: [-3, -1, 1, 2], target=1
Output: 0
Explanation: The triplet [-3, 1, 2] has the closest sum to the target.

Example 3:
Input: [1, 0, 1, 1], target=100
Output: 3
Explanation: The triplet [1, 1, 1] has the closest sum to the target.
"""
import math
from typing import List


class TripletSumCloseToTarget:
    @staticmethod
    def find_triplet_sum_to_target(nums: List[int], target: int) -> int:
        # Sort the array
        nums.sort()
        smallest_difference = math.inf
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums) - 1
            while left < right:
                target_diff = target - nums[i] - nums[left] - nums[right]
                if target_diff == 0:  # We've found a triplet with an exact sum
                    return target  # return sum of all the numbers
                # The second part of the following if it is to handle the smallest sum when we have more than one
                # solution.
                if abs(target_diff) < abs(smallest_difference) or (abs(target_diff) == abs(smallest_difference) and
                                                                   target_diff > smallest_difference):
                    smallest_difference = target_diff  # save the closest and the biggest difference

                if target_diff > 0:
                    left += 1  # we need a triplet with a bigger sum
                else:
                    right -= 1  # we need a triplet with a smaller sum
        return target - smallest_difference


def main():
    tsctt = TripletSumCloseToTarget()
    print(tsctt.find_triplet_sum_to_target([-2, 0, 1, 2], 2))
    print(tsctt.find_triplet_sum_to_target([-3, -1, 1, 2], 1))
    print(tsctt.find_triplet_sum_to_target([1, 0, 1, 1], 100))


main()


"""
Time Complexity: O(N*LogN) - Sorting + N*N ==> O(N^2)
Space Complexity: O(N)
"""
