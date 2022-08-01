"""
In problems where we deal with sorted arrays (or LinkedLists) and need to find a set of elements that fulfill certain
constraints, the Two Pointers approach becomes quite useful. The set of elements could be a pair, a triplet or even a
sub-array.

Problem Statement : Given an array, find the length of the smallest sub-array in it which when sorted will sort the
                    whole array.

Example 1:
Input: [1, 2, 5, 3, 7, 10, 9, 12]
Output: 5
Explanation: We need to sort only the sub-array [5, 3, 7, 10, 9] to make the whole array sorted

Example 2:
Input: [1, 3, 2, 0, -1, 7, 10]
Output: 5
Explanation: We need to sort only the sub-array [1, 3, 2, 0, -1] to make the whole array sorted

Example 3:
Input: [1, 2, 3]
Output: 0
Explanation: The array is already sorted

Example 4:
Input: [3, 2, 1]
Output: 3
Explanation: The whole array needs to be sorted.
"""
import math
from typing import List


class MinimumWindowSort:
    @staticmethod
    def shortest_window_sort(nums: List[int]) -> int:
        nums_length = len(nums)
        low = 0
        high = nums_length - 1
        # Find the first number out of the sorting order from the beginning
        while low < nums_length - 1 and nums[low] <= nums[low+1]:
            low += 1

        # If the array is already sorted
        if low == nums_length - 1:
            return 0

        # Find the first number out of the sorting order from the end
        while high > 0 and nums[high] >= nums[high-1]:
            high -= 1

        # Find the maximum and minimum of the sub-array.
        subarray_max = -math.inf
        subarray_min = math.inf
        for k in range(low, high+1):
            subarray_max = max(subarray_max, nums[k])
            subarray_min = min(subarray_min, nums[k])

        # Extend the sub-array to include any number which is bigger than the minimum of the sub-array.
        while low > 0 and nums[low-1] > subarray_min:
            low -= 1

        # Extend the sub-array to include any number which is smaller than the maximum of the sub-array.
        while high < nums_length - 1 and nums[high+1] < subarray_max:
            high += 1

        return high - low + 1


def main():
    mws = MinimumWindowSort()
    print(mws.shortest_window_sort([1, 2, 5, 3, 7, 10, 9, 12]))
    print(mws.shortest_window_sort([1, 3, 2, 0, -1, 7, 10]))
    print(mws.shortest_window_sort([1, 2, 3]))
    print(mws.shortest_window_sort([3, 2, 1]))


main()


"""
Time Complexity: N ==> O(N)
Space Complexity: O(1)
"""
