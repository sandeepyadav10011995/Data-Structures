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

Question: Given a string, find the length of the longest substring in it with no more than K distinct characters.

    Algo:
        1.  First, we will insert characters from the beginning of the string until we have K distinct characters
            in the HashMap.
        2.  These characters will constitute our sliding window. We are asked to find the longest such window having
            no more than K distinct characters. We will remember the length of this window as the longest window so far.
        3.  After this, we will keep adding one character in the sliding window (i.e., slide the window ahead) in a
            stepwise fashion.
        4.  In each step, we will try to shrink the window from the beginning if the count of distinct characters in
            the HashMap is larger than K. We will shrink the window until we have no more than K distinct characters in
            the HashMap. This is needed as we intend to find the longest window.
        5.  While shrinking, we’ll decrement the character’s frequency going out of the window and remove it from the
            HashMap if its frequency becomes zero.
        6.  At the end of each step, we’ll check if the current window length is the longest so far, and if so, remember
            its length.

Example:
Output:

------------------------------------------------------ CODE ------------------------------------------------------------
"""


class LongestSubstringKDistinctCharacters:
    @staticmethod
    def longest_substring_with_k_distinct(str1: str, K: int) -> int:
        max_length = 0
        window_start = 0
        char_freq = {}
        for window_end in range(len(str1)):
            right_char = str1[window_end]
            if right_char not in char_freq:
                char_freq[right_char] = 0
            char_freq[right_char] += 1
            # shrink the sliding window, until we are left with 'k' distinct characters in the char_frequency
            while len(char_freq) > K:
                left_char = str1[window_start]
                char_freq[left_char] -= 1
                if char_freq[left_char] == 0:
                    del char_freq[left_char]
                window_start += 1  # shrink the window
            # remember the max_length so far
            max_length = max(max_length, window_end - window_start + 1)
        return max_length


def main():
    lskdc = LongestSubstringKDistinctCharacters()
    print("Length of the longest sub-string: " + str(lskdc.longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest sub-string: " + str(lskdc.longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest sub-string: " + str(lskdc.longest_substring_with_k_distinct("cbbebi", 3)))


main()

"""
Overall TC : O(2N) --> O(N)
Overall SC: O(K+1) --> O(K)
"""
