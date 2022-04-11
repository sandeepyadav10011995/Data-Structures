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

Question: Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous
          sub-array of size ‘k’.
Example:
Output:

------------------------------------------------------ CODE ------------------------------------------------------------
"""
from typing import List


class MaxSumSubArray:
    @staticmethod
    def find_max_sum_sub_array(nums: List[int], k: int) -> int:
        max_sum = 0
        window_sum = 0
        window_start = 0
        for window_end in range(len(nums)):
            window_sum += nums[window_end]

            # slide the window, we don't need to slide if we've not hit the required window size of 'k'
            if window_end >= k-1:
                max_sum = max(max_sum, window_sum)  # update the max-sum
                window_sum -= nums[window_start]  # sub the element going out
                window_start += 1  # slide the window ahead

        return max_sum


def main():
    msa = MaxSumSubArray()
    print("Maximum sum of a sub-array of size K: " + str(msa.find_max_sum_sub_array([2, 1, 5, 1, 3, 2], 3)))
    print("Maximum sum of a sub-array of size K: " + str(msa.find_max_sum_sub_array([2, 3, 4, 1, 5], 2)))


main()


"""
Overall TC : O(2N) --> O(N)
Overall SC: O(1) --> O(1)
"""
