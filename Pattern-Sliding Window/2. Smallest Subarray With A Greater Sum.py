"""
------------------------------------------------ SLIDING WINDOW --------------------------------------------------------
Types of Sliding Window -:
1. Fixed Length : When k, i.e. sliding window size is provided as a constraint.
2. Dynamic Variant: Caterpillar

How to recognize these problems ?
Things we iterate over sequentially;
    a. Contiguous Sequence of elements.
    b. Sliding arrays, linked-lists

In terms of the way questions are asked ? => Min, Max, Largest, Shortest
Questions Variants
1. Fixed Length: Max Sub-array of size k
2. Dynamic Variant: Smallest Sum (equal to S) => Will need to use Auxiliary DS, i.e. Arrays or Hashmap
                    a. Largest sub-string with no more than k distinct characters.
                    b. String Permutations

Question: Given an array of positive numbers and a positive number ‘S,’ find the length of the smallest contiguous
          sub-array whose sum is greater than or equal to ‘S’. Return 0 if no such sub-array exists.

    Algo:
        1. First, we will add-up elements from the beginning of the array until their sum becomes greater than or
           equal to ‘S.’
        2. These elements will constitute our sliding window. We are asked to find the smallest such
           window having a sum greater than or equal to ‘S.’ We will remember the length of this window as the smallest
           window so far.
        3. After this, we will keep adding one element in the sliding window (i.e., slide the window
           ahead) in a stepwise fashion.
        4. In each step, we will also try to shrink the window from the beginning. We will
           shrink the window until the window’s sum is smaller than ‘S’ again. This is needed as we intend to find the
           smallest window. This shrinking will also happen in multiple steps; in each step, we will do two things:
                a. Check if the current window length is the smallest so far, and if so, remember its length.
                b. Subtract the first element of the window from the running sum to shrink the sliding window.

Example:
Output:

------------------------------------------------------ CODE ------------------------------------------------------------
"""
import math

from typing import List


class SmallestSubArraySum:
    @staticmethod
    def find_smallest_sub_array_sum(nums: List[int], S: int) -> int:
        min_length = math.inf
        window_sum = 0
        window_start, window_end = 0, 0
        for window_end in range(len(nums)):
            window_sum += nums[window_end]

            # slide the window, we don't need to slide if we've not hit the required window size of 'k'
            while window_sum >= S:
                min_length = min(min_length, window_end-window_start + 1)  # update the sub-array size
                window_sum -= nums[window_start]  # sub the element going out
                window_start += 1  # slide the window ahead
        # Edge Case
        if min_length == math.inf:
            return 0
        return min_length


def main():
    ssa = SmallestSubArraySum()
    print("Smallest sub-array length: " + str(ssa.find_smallest_sub_array_sum([2, 1, 5, 2, 3, 2], 7)))
    print("Smallest sub-array length: " + str(ssa.find_smallest_sub_array_sum([2, 1, 5, 2, 8], 7)))
    print("Smallest sub-array length: " + str(ssa.find_smallest_sub_array_sum([3, 4, 1, 1, 6], 8)))


main()

"""
Overall TC : O(2N) --> O(N)
Overall SC: O(1) --> O(1)
"""
