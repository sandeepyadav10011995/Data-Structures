"""
In problems where we deal with sorted arrays (or LinkedLists) and need to find a set of elements that fulfill certain
constraints, the Two Pointers approach becomes quite useful. The set of elements could be a pair, a triplet or even a
sub-array.

Problem Statement : Given a sorted array, create a new array containing squares of all the numbers of the input array in
                    the sorted order.

Algo : 


Example 1:
    Input: [-2, -1, 0, 1, 2, 3]
    Output: [0, 1, 1, 4, 4, 9]

Example 2:
    Input: [-3, -1, 0, 1, 2]
    Output: [0, 1, 1, 4, 9]

"""
from typing import List


class SquaringASortedArray:
    @staticmethod
    def make_squares(nums: List[int]) -> List[int]:
        nums_length = len(nums)
        squares = [0 for _ in range(nums_length)]
        highest_square_idx = nums_length - 1
        left, right = 0, nums_length - 1

        while left <= right:
            ls = nums[left] * nums[left]
            rs = nums[right] * nums[right]

            if ls > rs:
                squares[highest_square_idx] = ls
                left += 1
            else:
                squares[highest_square_idx] = rs
                right -= 1
            highest_square_idx -= 1

        return squares


"""
Time Complexity: O(N)
Space Complexity: O(N)
"""
