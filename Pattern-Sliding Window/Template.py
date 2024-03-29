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

Question: Given an array, find the average of all sub-arrays of ‘K’ contiguous elements in it.
Example:
Output:

------------------------------------------------------ CODE ------------------------------------------------------------
"""
from typing import List


class Average:
    @staticmethod
    def find_avg_of_sub_array(nums: List[int], k: int) -> List[float]:
        result = []
        window_sum = 0
        window_start, window_end = 0, 0
        for window_end in range(len(nums)):
            window_sum += nums[window_end]

            # slide the window, we don't need to slide if we've not hit the required window size of 'k'
            if window_end >= k-1:
                result.append(window_sum/k)  # calculate the avg
                window_sum -= nums[window_start]  # sub the element going out
                window_start += 1  # slide the window ahead

        return result


def main():
    avg = Average()
    result = avg.find_avg_of_sub_array([1, 3, 2, 6, -1, 4, 1, 8, 2], 5)
    print("Averages of sub-arrays of size K: " + str(result))


main()


"""
Overall TC : O(2N) --> O(N)
Overall SC: O(N) --> O(N)
"""
