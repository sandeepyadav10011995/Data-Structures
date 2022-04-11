"""
In problems where we deal with sorted arrays (or LinkedLists) and need to find a set of elements that fulfill certain
constraints, the Two Pointers approach becomes quite useful. The set of elements could be a pair, a triplet or even a
sub-array.

For example -: Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the
              given target. --> Two Sum
Bruteforce Approach -: N^2 --> NlogN (If we use Binary Search since the array is sorted)
Optimized Approach -: Given that the input array is sorted, an efficient way would be to start with one pointer in the
                      beginning and another pointer at the end. At every step, we will see if the numbers pointed by the
                      two pointers add up to the target sum. If they do not, we will do one of two things:
                        a. If the sum of the two numbers pointed by the two pointers is greater than the target sum,
                           this means that we need a pair with a smaller sum. So, to try more pairs, we can decrement
                           the end-pointer.
                        b. If the sum of the two numbers pointed by the two pointers is smaller than the target sum,
                           this means that we need a pair with a larger sum. So, to try more pairs, we can increment the
                           start-pointer.
Example 1:
    Input: [1, 2, 3, 4, 6], target=6
    Output: [1, 3]
    Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

Example 2:
    Input: [2, 5, 9, 11], target=11
    Output: [0, 2]
    Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11
"""
from typing import List


class TwoSum:
    @staticmethod
    def find_two_sum(nums: List[int], target_sum: int) -> list:
        left = 0
        right = len(nums)-1

        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == target_sum:
                return [left, right]
            elif current_sum < target_sum:
                left += 1  # we need a pair with a bigger sum
            else:
                right -= 1  # we need a pair with a smaller sum
        return [-1, -1]


"""
Time Complexity: O(N)
Space Complexity: O(1)
"""


"""
Follow Up: What if the array is not sorted ?
Approach: Using Hash Map
"""


class TwoSum2:
    @staticmethod
    def find_two_sum(nums: List[int], target: int) -> List[int]:
        nums_to_index = {}
        for i, num in enumerate(nums):
            if target-num in nums_to_index:
                return [nums_to_index[target-num], i]
            nums_to_index[num] = i


"""
Time Complexity: O(N)
Space Complexity: O(N)
"""


def main():
    ts = TwoSum()
    print(ts.find_two_sum([1, 2, 3, 4, 6], 6))
    print(ts.find_two_sum([2, 5, 9, 11], 11))


main()
