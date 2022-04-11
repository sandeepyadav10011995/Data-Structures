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

Question:   Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the
            length of the longest contiguous sub-array having all 1s.

    Algo:
        This problem follows the Sliding Window pattern and is quite similar to Longest Substring with same Letters
        after Replacement. The only difference is that, in the problem, we only have two characters (1s and 0s) in the
        input arrays.

    Following a similar approach, we’ll iterate through the array to add one number at a time in the window. We’ll also
    keep track of the maximum number of repeating 1s in the current window (let’s call it maxOnesCount). So at any time,
    we know that we can have a window with 1s repeating maxOnesCount times, so we should try to replace the remaining 0s.
    If we have more than ‘k’ remaining 0s, we should shrink the window as we are not allowed to replace more than ‘k’
    0s.

Example:
    Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
    Output: 6
    Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous sub-array of 1s having length 6.


------------------------------------------------------ CODE ------------------------------------------------------------
"""
from typing import List


class LongestSubarrayWithOnesReplacement:
    @staticmethod
    def length_of_longest_substring(array: List[int], k: int) -> int:
        max_length = 0
        window_start = 0
        max_ones_count = 0
        # try to extend the range [windowStart, windowEnd]
        for window_end in range(len(array)):
            if array[window_end] == 1:
                max_ones_count += 1
            # Current window size is from window_start to window_end, overall we have a maximum of 1s
            # repeating 'max_ones_count' times, this means we can have a window with 'max_ones_count' 1s
            # and the remaining are 0s which should replace with 1s.
            # now, if the remaining 0s are more than 'k', it is the time to shrink the window as we
            # are not allowed to replace more than 'k' 0s
            if window_end-window_start+1 - max_ones_count > k:
                if array[window_start] == 1:
                    max_ones_count -= 1
                window_start += 1
            max_length = max(max_length, window_end-window_start+1)
        return max_length


def main():
    lsr = LongestSubarrayWithOnesReplacement()
    print(lsr.length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    print(lsr.length_of_longest_substring([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))


main()

"""
Overall TC : O(N) --> O(N)
Overall SC: O(1) --> O(1)
"""
