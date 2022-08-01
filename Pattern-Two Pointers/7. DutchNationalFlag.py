"""
In problems where we deal with sorted arrays (or LinkedLists) and need to find a set of elements that fulfill certain
constraints, the Two Pointers approach becomes quite useful. The set of elements could be a pair, a triplet or even a
sub-array.

Problem Statement : Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the
                    array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.
                    The flag of the Netherlands consists of three colors: red, white and blue; and since our input array
                    also consists of three different numbers that is why it is called Dutch National Flag problem.

Algo: We can use a Two Pointers approach while iterating through the array. Let’s say the two pointers are called low
      and high which are pointing to the first and the last element of the array respectively. So while iterating, we
      will move all 0s before low and all 2s after high so that in the end, all 1s will be between low and high.

Example 1:
Input: [1, 0, 2, 1, 0]
Output: [0, 0, 1, 1, 2]

Example 2:
Input: [2, 2, 0, 1, 2, 0]
Output: [0, 0, 1, 2, 2, 2,]
"""
from typing import List
from collections import deque


class DutchNationalFlag:
    @staticmethod
    def dutch_flag_sort(nums: List[int]) -> List[int]:
        # all elements < low ==> 0 and,
        # all elements > high ==> 2
        # all elements from >= low and < i  ==> 1
        low = 0
        high = len(nums) - 1
        i = 0
        while i <= high:
            if nums[i] == 0:
                nums[i], nums[low] = nums[low], nums[i]
                # Increment "i" and "low"
                i += 1
                low += 1
            elif nums[i] == 1:
                i += 1
            else:  # The case for nums[i] == 2
                nums[i], nums[high] = nums[high], nums[i]
                # Decrement "high" only, after the swapping the number at index "i" ==> Ca be anything i.e, 0, 1, 2.
                high -= 1


def main():
    dnf = DutchNationalFlag()
    arr = [1, 0, 2, 1, 0]
    dnf.dutch_flag_sort(arr)
    print(arr)

    arr = [2, 2, 0, 1, 2, 0]
    dnf.dutch_flag_sort(arr)
    print(arr)


main()


"""
Time Complexity: N(for-loop)*N*N(creating sub-arrays) ==> O(N^3)
Space Complexity: O(N)
"""
