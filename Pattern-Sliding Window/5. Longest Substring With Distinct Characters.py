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

Question:   Given a string, find the length of the longest substring, which has all distinct characters.

    Algo:
        This problem follows the Sliding Window pattern, and we can use a similar dynamic sliding window strategy as
        discussed in Longest Substring with K Distinct Characters. We can use a HashMap to remember the last index of
        each character we have processed. Whenever we get a duplicate character, we will shrink our sliding window to
        ensure that we always have distinct characters in the sliding window.

Example:
Output:

------------------------------------------------------ CODE ------------------------------------------------------------
"""


class LongestSubstringDistinctCharacters:
    @staticmethod
    def non_repeat_substring(str1: str) -> int:
        max_length = 0
        window_start = 0
        char_index_map = {}
        # try to extend the range [windowStart, windowEnd]
        for window_end in range(len(str1)):
            right_char = str1[window_end]
            # if the map already contains the 'right_char', shrink the window from the beginning so that
            # we have only one occurrence of 'right_char'
            if right_char in char_index_map:
                # this is tricky; in the current window, we will not have any 'right_char' after its previous index
                # and if 'window_start' is already ahead of the last index of 'right_char', we'll keep 'window_start'
                window_start = max(window_start, char_index_map[right_char] + 1)
            # insert the 'right_char' into the map
            char_index_map[right_char] = window_end
            # remember the maximum length so far
            max_length = max(max_length, window_end - window_start + 1)
        return max_length


def main():
    lsdc = LongestSubstringDistinctCharacters()
    print("Length of the longest sub-string: " + str(lsdc.non_repeat_substring("aabccbb")))
    print("Length of the longest sub-string: " + str(lsdc.non_repeat_substring("abbbb")))
    print("Length of the longest sub-string: " + str(lsdc.non_repeat_substring("abccde")))


main()

"""
Overall TC : O(2N) --> O(N)
Overall SC: O(K) --> O(1)  # Bcz at max char_index_map will store only K=26 english alphabets. So K <= N and K max 
                             value is 26

"""
